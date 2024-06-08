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
