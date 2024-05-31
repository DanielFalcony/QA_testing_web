from zeep import Client, Settings
from conftest import data

wsdl = data["wsdl"]
settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


def check_text(text):
    response = client.service.checkText(text)
    print(response)
    return response[0]["s"]
