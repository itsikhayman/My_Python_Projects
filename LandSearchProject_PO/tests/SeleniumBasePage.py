from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class seleniumBasePage():

    def selenium_start(self):
        print("- Start Test -")
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options = Options()
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        # options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def selenium_end(self, driver):
        print("\n*** Press any key to close ***")
        input()
        print("- End Test -")
        driver.close()
        exit()
