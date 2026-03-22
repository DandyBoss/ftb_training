from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):

    Username_input = (By.ID,"username")
    Password_input = (By.ID, "password")
    Sign_in_btn = (By.CSS_SELECTOR, ".btn-primary")
    Logout_btn = (By.CSS_SELECTOR, ".btn-logout, a[href*='logout']")
    Register_link = (By.CSS_SELECTOR,"a[href*='register'], .register-link, a:contains('Register')")

    error_message = (By.CSS_SELECTOR,".form-error")

    def open_login_page(self):
        self.open("/login")
        return self

    def login(self,username,password):
        self.fill(self.Username_input,username)
        self.fill(self.Password_input,password)
        self.click(self.Sign_in_btn)
        return self
    #def is_logged_in(self):


    def logout(self):
        try:
            self.click(self.Logout_btn)
        except:
            pass
        return self

    def get_error_message(self):
        try:
            return self.get_text(self.error_message)
        except:
            return None

    def go_to_register(self):
        self.click(self.Register_link)
        return self
