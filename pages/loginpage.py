from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "user_name")
        self.password_field = (By.NAME, "user_password")
        self.login_button = (By.NAME, "Login")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def invalidLogin(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
