#do not change anything from this file except the driver path variable.

class Paths:
    driver_path = '/home/.../chromedriver_linux64/chromedriver'
    sign_in_page = 'https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin'

    username_css_selector = '#username'
    password_css_selector = '#password'
    login_button_path = '//*[@type="submit"]'

    job_page_link = 'https://www.linkedin.com/jobs'
    job_title_field_xpath = '//*[@placeholder="Search jobs"]'
    job_location_field_xpath = '//*[@placeholder="Search location"]'

    job_counter_path1 = "//div/div/section/div/div/div/div/div/div/ul/li["
    job_counter_path2 = "]"
    job_counter_path3 = "/div/artdeco-entity-lockup/artdeco-entity-lockup-content/h3/a"

    see_more_button_path = '//div[6]/div[3]/div[1]/div/div/div/div/div/div[3]/div/button/span'
    job_link_button_path = '//h1'
    job_title_xpath = '//div[2]/div[1]/h1'
    job_location_span_xpath = '//div[2]/div[1]/h3/span[3]'
    job_location_link_xpath = '//div[2]/div[1]/h3/a[3]'
    jd_xpath = '//article/div/div'
    company_xpath = '//div[2]/div[1]/h3/a'

    back_button = "window.history.go(-1)"

    profile_skill_show_more_path = '//body/div[5]/div[6]/div[3]/div/div/div/div/div[2]/div/div[2]/div[6]/div/section/div[2]/button/span[1]'

    industry_skill_div_path = '//*[@class="pv-skill-categories-section__expanded"]/div[1]/ol/li['
    tool_technology_path = '//*[@class="pv-skill-categories-section__expanded"]/div[2]/ol/li['
    interpersonal_skill_path = '//*[@class="pv-skill-categories-section__expanded"]/div[3]/ol/li['
    other_skill_path = '//*[@class="pv-skill-categories-section__expanded"]/div[4]/ol/li['

    skill_json_file_name = 'skill_data.json'
    jd_list = 'Linkedin_jd.json'

