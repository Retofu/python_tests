from selenium.webdriver.common.by import By
import pytest

@pytest.mark.selenium
def test_incorrect_login(driver):
    driver.get('https://magento.softwaretestingboard.com/customer/account/login/')
    email_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')
    button = driver.find_element(By.ID, 'send2')
    error_alert = driver.find_element(By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    email_field.send_keys('invalid_email@example.com')
    password_field.send_keys('wrong_password')
    button.click()
    assert error_alert.text == 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'