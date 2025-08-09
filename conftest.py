import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    yield driver

    if request.node.rep_call.failed:
        screenshot_name = f"screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_name)

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function")
def browser_chrome():
    driver = webdriver.Chrome()
    driver.get("http://localhost:100")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def browser_edge():
    service = Service(executable_path="C:\\Users\hp\PycharmProjects\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.get("http://localhost:100")
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Browser name (chrome or edge)')


@pytest.fixture(scope="function")
def browser(request):
    bd = request.config.getoption("--browser")
    print("Launching website")
    if bd == 'chrome':
        driver = webdriver.Chrome()
    else:
        service = Service(executable_path="C:\\Users\hp\PycharmProjects\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
    driver.get("http://localhost:100")
    yield driver
    driver.quit()
    print("close app")
