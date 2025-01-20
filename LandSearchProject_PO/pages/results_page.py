import csv, time, os, webbrowser, winsound
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LandSearchProject_PO.common.utils import utils

class resultsPage():
    def __init__(self, driver):  # constructor
        self.driver = driver   # every call to the functions need to deliver driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.landsearch.com/properties")

    def toggle_dark_mode(self):
        dark_mode_buttons_set = self.driver.find_elements(By.CSS_SELECTOR,'div[class*="header-dark"]')
        for button in dark_mode_buttons_set:
            if button.get_attribute('title') == 'Toggle dark mode':
                button.click()
                time.sleep(1)
                break

    def gather_properties_list(self):
        properties_set = self.driver.find_elements(By.CLASS_NAME, "preview__link")  # gather elements to properties_set
        property_list = []
        for property in properties_set:   # gather links to property_list set
            link = property.get_attribute("href")
            property_list.append(link)
        return property_list

    def scrape_data_function(self, selectors, property_link):
        field_values = [property_link] # first field on the row
        for by_method, selector in selectors:
            try:
                element = self.wait.until(EC.element_to_be_clickable((by_method, selector)))
                field_values.append(str(element.text))
            except Exception:
                field_values.append("N/A")  # missing data in the ad will be marked as N/A
        return field_values

    def scrape_data_from_property_list(self, property_list):
        csv_file_name = f"landsearch_properties_data_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.csv" # give csv a meaningful name
        user_input = input(f"Do you want to CSV scrape the first 3 properties? (type 'y' for yes): ")
        if user_input != 'y':
            print("Exiting...")
            exit()
        with open(csv_file_name, mode='w', newline='', encoding='utf-8') as csv_file:  # open csv file for data
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Property Link', 'Parcel Number', 'Price', 'Acreage', 'Seller', 'Team', 'Phone', 'Property Status'])  # headers
            counter = 1
            for property_link in property_list:
                print(f"Scraping Data {counter}: {property_link}")
                self.driver.get(property_link)  # open each link url to scrape data
                time.sleep(1)
                selectors = [  # List of tuples
                    (By.XPATH,'//li[contains(@class, "g-fc") and contains(@class, "$propertyCopy") and @data-label="parcel number"]'),  # Get parcel number
                    (By.CLASS_NAME, 'property-price'),
                    (By.CLASS_NAME, 'property-size'),
                    (By.CLASS_NAME, 'profile-card__name'),  # Get the land broker agent
                    (By.CLASS_NAME, 'profile-card__teams'), # Get the land broker agency
                    (By.CLASS_NAME, 'profile-card__phone'),
                    (By.CLASS_NAME, 'property-status'),
                ]
                field_values = self.scrape_data_function(selectors, property_link) # scrape data from each link
                csv_writer.writerow(field_values) # add the scraped data to csv
                #csv_file.flush() #Remark in real time
                if counter == 3:
                    utils.play_sound("tada.wav")  # play finish ringtone
                    return csv_file_name
                    break   # break from for
                counter += 1