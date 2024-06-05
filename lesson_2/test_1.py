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
    site.quit()
    assert text == err1


def test_step2(x_selector1, x_selector2, btn_selector, x_selector4, success):
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
    site.quit()
    assert text == success


