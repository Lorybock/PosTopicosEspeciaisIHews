from paginas.locators.elem_news import Elements
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def elem_found(self, elem):
        return WebDriverWait(self, 20).until(EC.presence_of_element_located((
            elem
        )))