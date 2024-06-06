import time

import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_step1(x_selector1, x_selector2, btn_selector, x_selector3, err1):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test2")
    btn = site.find_element("css", btn_selector)
    btn.click()
    error_label = site.find_element("xpath", x_selector3)
    text = error_label.text
    assert text == err1


def test_step2(x_selector1, x_selector2, x_selector4, x_selector5,
               x_selector6, x_selector7, x_selector8,
               btn_selector, btn_selector_pst, success, success_pst, btn_selector_save_pst):
    res = []
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["username"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    user_label = site.find_element("xpath", x_selector4)
    text = user_label.text
    res.append(True if text == success else False)
    btn = site.find_element("css", btn_selector_pst)
    btn.click()
    time.sleep(testdata["sleep_time"])
    input1 = site.find_element("xpath", x_selector5)
    input1.clear()
    input1.send_keys("qefqefsdafesdfews")
    input2 = site.find_element("xpath", x_selector6)
    input2.clear()
    input2.send_keys("dsadwqdqwdsadasf")
    input3 = site.find_element("xpath", x_selector7)
    input3.clear()
    input3.send_keys("dsadwqfqfewffsd")
    btn = site.find_element("xpath", btn_selector_save_pst)
    btn.click()
    time.sleep(testdata["sleep_time"])
    title_ex = site.find_element("xpath", x_selector8)
    title = title_ex.text
    res.append(True if title == success_pst else False)
    site.quit()
    assert all(res), "FAIL"


