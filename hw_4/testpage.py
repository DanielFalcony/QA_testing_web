import time

import requests

from BaseApp import BasePage, APIBasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class APIOperationsHelper(APIBasePage):
    def show_posts(self, params, test_text):
        headers = {"X-Auth-Token": self.login()}
        logging.info("Successfully login with token")
        try:
            res = requests.get(self.base_url + "/api/posts", params=params, headers=headers)
            logging.info(f"Get response: {res.status_code}")
        except:
            logging.exception("Error while get response")
            return False
        try:
            list_res = [i["title"] for i in res.json()["data"]]
            logging.info(f"Get list of posts: {list_res}")
        except:
            logging.exception("Error while get list of posts")
            return False
        result = True if test_text in list_res else False
        logging.info(f"Result: {result}")
        return result


class TestSearchLocators:
    ids = {}
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element: {locator}, not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Error: {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f"Exception with click button: {element_name}")
            return False
        logging.debug(f"Clicked button: {element_name}")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        time.sleep(1)
        field = self.find_element(locator, time=3.5)
        if not field:
            logging.error(f"Element: {locator}, not found")
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from: {element_name}")
            return None
        logging.debug(f"We find text: {text} in field: {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"],
                                   word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASSWORD_FIELD"],
                                   word, description="password form")

    def enter_post_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_TITLE_FIELD"],
                                   word, description="post title form")

    def enter_post_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_DESCRIPTION_FIELD"],
                                   word, description="post description form")

    def enter_post_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT_FIELD"],
                                   word, description="post content form")

    def enter_contact_us_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_US_NAME_FIELD"],
                                   word, description="contact us name form")

    def enter_contact_us_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_US_EMAIL_FIELD"],
                                   word, description="contact us email form")

    def enter_contact_us_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_US_CONTENT_FIELD"],
                                   word, description="contact us content form")

    # CLICK

    def click_login_button(self):
        logging.info("Click login button")
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"],
                          description="login button")

    def add_new_post(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ADD_NEW_POST_BTN"],
                          description="add new post button")

    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_POST_BTN"],
                          description="save new post button")

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"],
                          description="contact us button")

    def click_contact_us_send_msg_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_SEND_MSG_BTN"],
                          description="contact us send msg button")

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"],
                                          description="error field")

    def get_current_user(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CHECK_CURRENT_USER"],
                                          description="current user")

    def get_current_post_name(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_NEW_POST_NAME"],
                                          description="current post name")

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(f"Get alert text: {text}")
        return text


