from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver,base_url="https:/ftb.mentorpiece.org"):
        self.driver=driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver,10)

    def open(self,path):
        self.driver.get(f"{self.base_url}{path}")

    def find_element(self,locator,timeout=10):
        return self.wait.until(EC.presence_of_element_located(locator),message=f" Element not found: {locator}")

    def click(self,locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def fill(self,locator,text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return self.find_element(locator).text

    def get_current_url(self):
        return self.driver.current_url