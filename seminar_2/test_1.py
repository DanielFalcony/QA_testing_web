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


