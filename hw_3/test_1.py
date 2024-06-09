import time
from BaseApp import testdata
from testpage import OperationsHelper
import logging


def test_step1(browser):
    logging.info("Test step 1")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test2")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test step 2")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["username"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    assert True if testpage.get_current_user() == f"Hello, {testdata['username']}" else False


def test_step3(browser):
    logging.info("Test step 3")
    testpage = OperationsHelper(browser)
    testpage.add_new_post()
    testpage.enter_post_title("This is new post")
    testpage.enter_post_description("Some description of post")
    testpage.enter_post_content("And here is some content for post")
    testpage.click_save_post_button()
    assert True if testpage.get_current_post_name() == "This is new post" else False


def test_step4(browser):
    logging.info("Test step 4")
    testpage = OperationsHelper(browser)
    testpage.click_contact_us_button()
    testpage.enter_contact_us_name("Test")
    testpage.enter_contact_us_email("hzdkv@example.com")
    testpage.enter_contact_us_content("some content")
    testpage.click_contact_us_send_msg_button()
    time.sleep(testdata["sleep_time"])
    testpage.get_alert()
    assert True if testpage.get_alert() == "Form successfully submitted" else False

