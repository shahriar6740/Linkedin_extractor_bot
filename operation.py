from paths import Paths
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json


class Operation:

    driver = webdriver.Chrome(Paths.driver_path)

    def login(self, username, password):

        try:
            self.driver.get(Paths.sign_in_page)
            sleep(1)
            username_field = self.driver.find_element_by_css_selector(Paths.username_css_selector)

            password_field = self.driver.find_element_by_css_selector(Paths.password_css_selector)

            username_field.send_keys(username)
            password_field.send_keys(password)

            log_in_button = self.driver.find_element_by_xpath(Paths.login_button_path)
            log_in_button.click()
            sleep(2)
        except:
            print("Error in login")

    def job_search(self, search_title, location):

        try:
            self.driver.get(Paths.job_page_link)
            sleep(1)

            job_title_field = self.driver.find_element_by_xpath(Paths.job_title_field_xpath).send_keys(search_title)
            location_field = self.driver.find_element_by_xpath(Paths.job_location_field_xpath).send_keys(location, Keys.ENTER)
            sleep(3)
        except:
            print("job search failed")

    def make_dictionary(self, job_title, company_name, job_loc, job_description):

        key = ['position', 'company_name', 'location', 'description']
        value = [job_title, company_name, job_loc, job_description]
        return dict(zip(key, value))

    def dump_to_json(self, filename, data):
        with open(filename, 'a') as f:
            json.dump(data, f)
            f.write('\n')
            f.close()

    def scroll_page(self):

        #last_height = self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0, 4000):
            self.driver.execute_script("window.scrollTo(0," + str(i) + ")")
            i += 300

    def find_job_description(self):
        try:

            for i in range(1, 25):
                s1 = str("//div/div/section/div/div/div/div/div/div/ul/li[" + str(i) + "]"+"/div/artdeco-entity-lockup/artdeco-entity-lockup-content/h3/a")
                print(s1)
                currentjob = self.driver.find_element_by_xpath(s1).click()
                print('current job clicked')

                job_link = self.driver.find_element_by_xpath(Paths.job_link_button_path).click()
                sleep(0.5)
                see_more = self.driver.find_element_by_xpath(Paths.see_more_button_path).click()
                

                job_title = self.driver.find_element_by_xpath(Paths.job_title_xpath).text
                try:
                    job_loc = self.driver.find_element_by_xpath(Paths.job_location_span_xpath).text
                except:
                    job_loc = self.driver.find_element_by_xpath(Paths.job_location_link_xpath).text

                job_description = self.driver.find_element_by_xpath(Paths.jd_xpath).text
                company_name = self.driver.find_element_by_xpath(Paths.company_xpath).text

                data = self.make_dictionary(job_title, company_name, job_loc, job_description)
                print('data dict created')
                self.dump_to_json(Paths.jd_list, data)

                self.driver.execute_script("window.history.go(-1)")

                sleep(1)

            self.driver.close()
        except:
            print("Error in extracting job descriptions")
            self.driver.close()

    def pagination(self):
        job_page = self.driver.current_url
        print('pagination loaded')
        if job_page :
            try:
                self.find_job_description()
            except:
                print('error in 1st page extraction \n')

            i=25
            while True:
                page = job_page + '&start='+ str(i)
                if page:
                    try:
                        self.driver.get(page)
                        sleep(1)
                        self.find_job_description()
                        i += 25
                    except:
                        print("error in "+ i + 'th page extraction \n')
                else:
                    break

        else:
            print('job page not found')
            







    def import_profile_link_from_csv(self):
        try:
            import pandas as pd
            df = pd.read_csv('Profile_link.csv', usecols=['profile_link'])
            df = df.T
            linkedin_id_list = df.values.tolist()
            linkedin_id_list = linkedin_id_list[0]
            return linkedin_id_list

        except:
            print("error in loading csv file")

    
    def create_skill_list(self, path):

        skill_counter = 1
        skill_list = []
        try:
            while True:
                value = self.driver.find_element_by_xpath(path + str(skill_counter) + ']/div/div/p').text
                skill_list.append(value)
                skill_counter += 1
                if self.driver.find_element_by_xpath(path + str(skill_counter) + ']'):
                    continue
                else:
                    break
            print(skill_list)
        except:
            print('error in loading industry knowledge skill')
        return skill_list


    def show_skill(self):

        id_list = self.import_profile_link_from_csv()
        print(id_list)
        for i in range(len(id_list)):
            print(id_list[i])
            self.driver.get(id_list[i])
            sleep(1)
            self.scroll_page()

            try:
                see_more_skill_button_click = self.driver.find_element_by_xpath(
                    Paths.profile_skill_show_more_path).click()

                industry_skill_list = self.create_skill_list(Paths.industry_skill_div_path)
                tools_and_technologies = self.create_skill_list(Paths.tool_technology_path)
                interpersonal_skill = self.create_skill_list(Paths.interpersonal_skill_path)
                other_skill = self.create_skill_list(Paths.other_skill_path)

                key = ['industry knowledge', 'tools and technologies', 'Interpersonal Skills', 'other skill']
                values = [industry_skill_list, tools_and_technologies, interpersonal_skill, other_skill]

                final_keys = ['profile_link', 'skills']
                final_values = [id_list[i], dict(zip(key, values))]
                final_dict = dict(zip(final_keys, final_values))

                self.dump_to_json(Paths.skill_json_file_name, final_dict)
                sleep(1)
            except:
                print('problem in loading')
            language_counter = 1

            try:
                while self.driver.find_element_by_xpath('//*[@class="pv-accomplishments-block__content break-words"]/div/ul/li[' + str(language_counter) + ']//h4/span'):
                    lang = self.driver.find_element_by_xpath('//*[@class="pv-accomplishments-block__content break-words"]/div/ul/li[' + str(language_counter) + ']//h4/span').text
                    type = self.driver.find_element_by_xpath('//*[@class="pv-accomplishments-block__content break-words"]/div/ul/li[1]/p').text

                    v1 = dict(zip(lang, type))
                    print(v1)
                    language_counter += 1
            except:
                print('lang not loaded')



        self.driver.close()










