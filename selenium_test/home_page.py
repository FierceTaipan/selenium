# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ChromeOptions


@pytest.fixture
def driver(request):
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    firefox_capabilities['binary'] = '/usr/bin/firefox'
    driver = webdriver.Firefox(capabilities=firefox_capabilities)
    request.addfinalizer(driver.quit)
    return driver


def test_ex(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("selenium")
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 100).until(EC.title_is("selenium - Поиск в Google"))

#  '/snap/bin/chromium'
#  '/urs/local/bin/chromedriver'

# @pytest.fixture
# def driver(request):
#     options = webdriver.ChromeOptions()
#     chrome_path = '/snap/bin/chromium'
#     driver_path = '/urs/local/bin/chromedriver'
#     options.driver_path = driver_path
#     options.add_argument("--no-default-browser-check")
#     options.add_argument("--no-first-run")
#     options.add_argument("--disable-default-apps")
#     options.add_argument("--verbose")
#     wd = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)
#     request.addfinalizer(wd.quit)
#     return wd
#
#
# def test_example(driver):
#     driver.get("http://www.google.com/")
#     driver.find_element_by_name("q").send_keys("selenium")
#     driver.find_element_by_name("btnG").click()
#     WebDriverWait(driver, 10).until(EC.title_is("selenium - Поиск в Google"))
