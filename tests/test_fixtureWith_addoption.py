import time

from selenium.webdriver.common.by import By


class Test_FixtureWith_addoption:
    def test_login(self, browser):
        browser.find_element(By.NAME, "user_name").send_keys("admin")
        browser.find_element(By.NAME, "user_password"). send_keys("admin")
        browser.find_element(By.NAME, "Login").click()
        time.sleep(5)
