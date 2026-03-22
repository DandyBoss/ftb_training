from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base_page import BasePage

class RegisterPage(BasePage):

    First_name = (By.ID,"firstname")
    Last_name = (By.ID, "lastname")
    Middle_name = (By.ID, "middlename")
    Username = (By.ID, "username")
    Email = (By.ID, "email")
    Password = (By.ID, "password")

    Create_account_btn=(By.CSS_SELECTOR,"button[type='submit'")
    Back_to_login_link= (By.CSS_SELECTOR,".btn-cansel")


    Success_message = (By.CSS_SELECTOR,".alert-success,.success,[role='status'")
    Error_message = (By.CSS_SELECTOR,"form-error span")

    def open_register_page(self):
        self.open("/register")
        return self

    def fill_registration_form(self,first_name,last_name,username,email,password):
        self.fill(self.First_name,first_name)
        self.fill(self.Last_name,last_name)
        self.fill(self.Username,username)
        self.fill(self.Email,email)
        self.fill(self.Password,password)
        return self

    def submit_registration(self):
        self.click(self.Create_account_btn)
        return self

    def is_registration_successful(self):
        if "/login" in self.get_current_url():
                return True
        try:
            self.find_element(self.Success_message,timeout=3)
            return True
        except:
            return False

    def get_error_message(self):
        try:
            xpath = "//input[@id='username']/following-sibling::div[@class='form-error']//span"
            error = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            text = error.text.strip()
            if text:
                return text
        except:
            pass

    def go_to_login(self):
        self.click(self.Back_to_login_link)
        return self
