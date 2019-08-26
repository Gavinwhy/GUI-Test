from selenium import webdriver


# 多浏览器
# 调取webdriver驱动 - 02
class setupWD:
    #单例模式:确保只有一个实例在运行
    # if wd is None:
    @classmethod
    def get_wd(cls, browser='firefox'):
        # 如果driver没有实例化,则进行实例化,否则,直接返回
        # 打不开第二个浏览器
        # if cls.wd is None:
        if browser == 'ie':
            cls.wd = webdriver.Ie(executable_path=r"E:\selenium\IEDriverServer.exe")

        elif browser == 'chrome':
            cls.wd = webdriver.Chrome(executable_path=r"E:\selenium\chromedriver.exe")

        else:
            cls.wd = webdriver.Firefox(firefox_binary=r"E:\Program Files\Mozilla Firefox\firefox.exe", executable_path=r"E:\selenium\geckodriver.exe")

        url = ""
        cls.wd.get(url)
        cls.wd.maximize_window()
        cls.wd.set_page_load_timeout(10)
        cls.wd.set_script_timeout(10)
        cls.wd.implicitly_wait(10)

        return cls.wd

    def quit(self):
        self.wd.quit()

    def __del__(self):
        self.wd.quit()