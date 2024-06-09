import time

from BaseApp import BasePage, testdata
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_CHECK_CURRENT_USER = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_ADD_NEW_POST_BTN = (By.CSS_SELECTOR, """#create-btn""")
    LOCATOR_POST_TITLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_POST_DESCRIPTION_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_POST_CONTENT_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_NEW_POST_NAME = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_US_BTN = (By.CSS_SELECTOR, """li:nth-child(2)""")
    LOCATOR_CONTACT_US_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_US_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_US_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_SEND_MSG_BTN = (By.CSS_SELECTOR, """div.submit""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASSWORD_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASSWORD_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD)
        text = error_field.text
        logging.info(f"Get error text: {text}, in error field: {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_current_user(self):
        current_user = self.find_element(TestSearchLocators.LOCATOR_CHECK_CURRENT_USER)
        text = current_user.text
        logging.info(
            f"Get current user: {text}, in current user field: {TestSearchLocators.LOCATOR_CHECK_CURRENT_USER[1]}")
        return text

    def add_new_post(self):
        logging.info("Click add new post button")
        self.find_element(TestSearchLocators.LOCATOR_ADD_NEW_POST_BTN, time=3).click()

    def enter_post_title(self, title):
        logging.info(f"Send: {title}, to element: {TestSearchLocators.LOCATOR_POST_TITLE_FIELD[1]}")
        post_title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE_FIELD)
        post_title_field.clear()
        post_title_field.send_keys(title)

    def enter_post_description(self, description):
        logging.info(f"Send: {description}, to element: {TestSearchLocators.LOCATOR_POST_DESCRIPTION_FIELD[1]}")
        post_description_field = self.find_element(TestSearchLocators.LOCATOR_POST_DESCRIPTION_FIELD)
        post_description_field.clear()
        post_description_field.send_keys(description)

    def enter_post_content(self, content):
        logging.info(f"Send: {content}, to element: {TestSearchLocators.LOCATOR_POST_CONTENT_FIELD[1]}")
        post_content_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT_FIELD)
        post_content_field.clear()
        post_content_field.send_keys(content)

    def click_save_post_button(self):
        logging.info("Click save post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_current_post_name(self):
        time.sleep(testdata["sleep_time"])
        post_name = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_NAME)
        text = post_name.text
        logging.info(f"Get post name: {text}, in post name field: {TestSearchLocators.LOCATOR_NEW_POST_NAME[1]}")
        return text

    def click_contact_us_button(self):
        logging.info("Click contact us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def enter_contact_us_name(self, name):
        logging.info(f"Send: {name}, to element: {TestSearchLocators.LOCATOR_CONTACT_US_NAME_FIELD[1]}")
        contact_us_name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_NAME_FIELD)
        contact_us_name_field.clear()
        contact_us_name_field.send_keys(name)

    def enter_contact_us_email(self, email):
        logging.info(f"Send: {email}, to element: {TestSearchLocators.LOCATOR_CONTACT_US_EMAIL_FIELD[1]}")
        contact_us_email_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_EMAIL_FIELD)
        contact_us_email_field.clear()
        contact_us_email_field.send_keys(email)

    def enter_contact_us_content(self, content):
        logging.info(f"Send: {content}, to element: {TestSearchLocators.LOCATOR_CONTACT_US_CONTENT_FIELD[1]}")
        contact_us_content_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_CONTENT_FIELD)
        contact_us_content_field.clear()
        contact_us_content_field.send_keys(content)

    def click_contact_us_send_msg_button(self):
        logging.info("Click contact us send msg button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_SEND_MSG_BTN).click()

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(f"Get alert text: {text}")
        return text
