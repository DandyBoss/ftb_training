import pytest
import random
import string
import time
from register_page import RegisterPage
from login_page import LoginPage

def generate_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
def generate_email():
    return f"test_{generate_string(8)}@example.com"
def generate_username():
    return f"testuser_{generate_string(6)}"


@pytest.mark.smoke
@pytest.mark.registration
class TestRegistration:


    def test_register_existing_username(self,driver):
        register_page=RegisterPage(driver)
        existing_username = "12345"

        register_page.open_register_page()
        register_page.fill_registration_form(
            first_name = "Test",
            last_name = "Duplicate",
            username = existing_username,
            email=generate_email(),
            password="SecurePass123!"
        )
        register_page.submit_registration()
        time.sleep(1)

        error = register_page.get_error_message()
        print(f"\n'{error}'")
        assert error is not None
    def test_register_empty_required_fields(self,driver):

        register_page=RegisterPage(driver)

        register_page.open_register_page()
        register_page.submit_registration()

        error_message = register_page.get_error_message()
        if error_message is None:
            email_field = driver.find_element(*RegisterPage.Email)
            validation_msg = email_field.get_property("validationMessage")
            assert validation_msg !=""
        else:
            assert error_message!=""

    def test_register_new_user_success(self, driver):

        page = RegisterPage(driver)

        page.open_register_page()
        page.fill_registration_form(
            first_name="Test",
            last_name="User",
            username=f"test_{generate_string()}",
            email=f"test_{generate_string()}@example.com",
            password="SecurePass123!"
        )
        page.submit_registration()

        import time
        time.sleep(2)

        print(f"\n🔍 URL после регистрации: {driver.current_url}")

        assert "/login" in driver.current_url, \
            f"Ожидали /login, получили: {driver.current_url}"