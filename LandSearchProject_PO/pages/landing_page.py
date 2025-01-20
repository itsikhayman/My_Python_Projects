import json, time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class landingPage():
    def __init__(self, driver):  # constructor
        self.driver = driver   # every call to the functions need to deliver driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.landsearch.com/")

    def click_login_button(self,by_method, by_locator):
        self.driver.find_element(by_method, by_locator).click()

    def populate_field(self, by_method, selector, value):
        element = self.wait.until(
            EC.presence_of_element_located((by_method, selector))
        )
        element.send_keys(value)

    def click_function(self, by_method, selector):
        element = self.wait.until(
            EC.element_to_be_clickable((by_method, selector))
        )
        element.click()

    def keyboard_function(self, by_method, selector, key):
        self.driver.find_element(by_method, selector).send_keys(key)

    def toggle_dark_mode(self):
        dark_mode_buttons_set = self.driver.find_elements(By.CSS_SELECTOR,'div[class*="header-dark"]')
        for button in dark_mode_buttons_set:
            if button.get_attribute('title') == 'Toggle dark mode':  # Adjust condition as needed
                button.click()
                time.sleep(1)
                break

    def register_to_site(self, user_details_json_file):
        # Click the 'Sign up' button
        self.click_function(By.LINK_TEXT, "Sign up")
        time.sleep(1)
        # fill registration form
        with open(user_details_json_file, 'r') as json_file:  # Take user details from JSON file
            reg_fields = json.load(json_file)
        for field in reg_fields:  # Populate registration fields
            self.populate_field(By.ID, field['register_selector'], field['value'])
        self.click_function(By.CLASS_NAME, "switch.g-s-3")  # switch checkbox to professional
        self.click_function(By.CLASS_NAME, "g-f")  # click signup
        self.keyboard_function(By.TAG_NAME, "body", Keys.ESCAPE) #close signup popup

    def login_to_site(self, user_details_json_file):
        # Click the 'Log in' button
        self.click_function(By.LINK_TEXT, "Log in")
        time.sleep(1)
        # fill registration form
        with open(user_details_json_file, 'r') as json_file:  # Take user details from JSON file
            login_fields = json.load(json_file)
        for field in login_fields:  # Populate login fields
            if field['login_selector'] == 'login_email':
                self.populate_field(By.ID, field['login_selector'], field['value'])
            elif field['login_selector'] == 'password':
                self.populate_field(By.ID, field['login_selector'], field['value'])
        self.keyboard_function(By.ID, "password", Keys.RETURN)  # click enter to continue
        time.sleep(1)

    def click_search_button(self):
        self.click_function(By.CLASS_NAME, "home-search__button")
        time.sleep(1)