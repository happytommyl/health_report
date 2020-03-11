from selenium import webdriver


##  读取用户名和密码
with open("/home/tommy/health/config.ini", mode='r', encoding='utf-8') as f:
    username, passwd = f.readline().split(",")
    print(username,passwd)



def access():
    ##  初始化浏览器设置
    # options = webdriver.FirefoxOptions()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # browser = webdriver.Firefox(options=options,executable_path='/home/tommy/health/geckodriver')
    # browser = webdriver.Edge()
    browser = webdriver.Chrome(options=options,executable_path='/home/tommy/health/chromedriver')
    ##  访问主页
    browser.get(url='http://jktb.cdutcm.edu.cn/#/login')
    browser.implicitly_wait(30)

    ##  登录
    a = browser.find_elements_by_class_name("el-input__inner")
    a[0].send_keys(username)
    a[1].send_keys(passwd)
    browser.find_element_by_class_name('submitButton').click()

    ##  填表
    b = browser.find_elements_by_class_name("el-radio__label")
    d = browser.find_elements_by_class_name("el-checkbox__label")
    try:
        c = browser.find_element_by_class_name("submitButton")
        for t in b:
            if t.text == "否":
                # print(t)
                t.click()
            if t.text == "健康":
                # print(t)
                t.click()
            if t.text == "正常":
                # print(t)
                t.click()
            if t.text == "无以上接触史":
                # print(t.text)
                t.click()
        for t in d:
            if t.text == "健康、无异常症状":
                # print(t.text)
                t.click()
        ##  提交
        c.click()
    except:
        print("今日已经提交")

    finally:
        # pass
        browser.close()

if __name__ == "__main__":
    access()
