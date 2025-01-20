import time
from LandSearchProject_PO.pages.landing_page import landingPage
from LandSearchProject_PO.pages.results_page import resultsPage
from LandSearchProject_PO.tests.SeleniumBasePage import seleniumBasePage
from LandSearchProject_PO.common.utils import utils


class projectLandsearchTest:
    # Globals
    base = seleniumBasePage()
    driver = base.selenium_start()
    user_details_json_file="user_details.json"

    # Open Landing page and use its classes
    landing_page = landingPage(driver)
    landing_page.toggle_dark_mode()  # toggle dark mode
    landing_page.register_to_site(user_details_json_file)  # register using a json file
    landing_page.login_to_site(user_details_json_file) # login using a json file
    landing_page.click_search_button() # forwarding to result page

    # Open Result page and use its classes
    result_page = resultsPage(driver)
    result_page.toggle_dark_mode()  # toggle dark mode
    property_list = result_page.gather_properties_list()  # create property list
    csv_file_name = result_page.scrape_data_from_property_list(property_list)  # scrape data to csv file
    utils.open_csv_file(csv_file_name) # present the csv file to user

    base.selenium_end(driver)
