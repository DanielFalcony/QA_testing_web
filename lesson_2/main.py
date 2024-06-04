import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


xpath = '//*[@id="login"]/div[3]/button'
print(site.get_element_property("xpath", xpath, "color"))

css_selector = "span.mdc-text-field__ripple"
print(site.get_element_property("css", css_selector, 'height'))
