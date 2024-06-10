import logging
import requests
import yaml
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class APIBasePage:
    def __init__(self):
        self.base_url = testdata["address"]
        self.username = testdata["username"]
        self.password = testdata["password"]

    def login(self):
        try:
            result = requests.post(self.base_url + "/gateway/login",
                                   data={"username": self.username, "password": self.password})
        except:
            logging.exception(f"Login fail exception")
            return None
        if result.status_code != 200:
            logging.exception(f"Login failed with status code {result.status_code}")
            return None
        else:
            logging.info(f"Login successful with status code {result.status_code}")
        return result.json()["token"]


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata["address"]

    def find_element(self, locator, time=3.5):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Element not found by {locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.exception(f"Property {property} not found in element with locator {locator}")
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Alert not found")
            return None
