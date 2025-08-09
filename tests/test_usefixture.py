from selenium.webdriver.common.by import By
from selenium import webdriver


class Test_fixtures:

    def test_login_chrome(self, browser_chrome):
        browser_chrome.find_element(By.NAME, "user_name").send_keys("admin")
        browser_chrome.find_element(By.NAME, "user_password").send_keys("admin")
        browser_chrome.find_element(By.NAME, "Login").click()

    def test_login_browser(self, browser_edge):
        browser_edge.find_element(By.NAME, "user_name").send_keys("admin")
        browser_edge.find_element(By.NAME, "user_password").send_keys("admin")
        browser_edge.find_element(By.NAME, "Login").click()