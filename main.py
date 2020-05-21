import config as cf


try:
    if cf.username == '' or cf.password == '' or cf.search_title == '' or cf.location == '':
        print("Please fill all the fields in the configuration.py file \n")

    else:
        from operation import Operation
        Operation_Object = Operation()

        Operation_Object.login(cf.username, cf.password)
        Operation_Object.job_search(cf.search_title, cf.location)
        Operation_Object.pagination()
        #Operation_Object.find_job_description()
        #Operation_Object.show_skill()
except:
    print("methods not found")



