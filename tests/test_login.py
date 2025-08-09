from pages.loginpage import LoginPage
from selenium.webdriver.common.by import By


def test_valid_login(driver):
    login_page = LoginPage(driver)
    driver.get("http://localhost:100")
    login_page.login("admin", "admin")
    assert "vtiger CRM - Commercial Open Source CRM" in driver.title


def test_invalid_login(driver):
    invalidLogin_page = LoginPage(driver)
    driver.get("http://localhost:100")
    invalidLogin_page.invalidLogin("admin2", "admin")
    assert driver.find_element(By.XPATH, "//td[contains(text(), 'username and password')]").is_displayed() == True

