import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


class Test_parallel_exec:

    def test_launch_website_chrome(self, browser_chrome):
        browser_chrome.find_element(By.NAME, "user_name").send_keys("admin")
        time.sleep(5)

    def test_launch_website_edge(self, browser_edge):
        browser_edge.find_element(By.NAME, "user_name").send_keys("admin")
        time.sleep(5)