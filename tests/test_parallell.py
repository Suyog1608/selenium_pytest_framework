import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service


class Test_parallel_exec:

    def test_launch_website_chrome(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:100")
        time.sleep(5)
        driver.quit()

    def test_launch_website_edge(self):
        service = Service(executable_path="C:\\Users\hp\PycharmProjects\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
        driver.get("http://localhost:100")
        time.sleep(5)
        driver.quit()

