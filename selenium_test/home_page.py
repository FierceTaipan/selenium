# -*- coding: utf-8 -*-
import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver(request):
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
#   firefox_capabilities['binary'] = '/usr/bin/firefox'
    firefox_capabilities['binary'] = '/Applications/Firefox.app/Contents/MacOS/firefox'
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(capabilities=firefox_capabilities, options=options)
    request.addfinalizer(driver.quit)
    return driver


def test_ex(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("selenium")
    time.sleep(5)
    driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 100).until(EC.title_is("selenium - Поиск в Google"))

#  '/snap/bin/chromium'
#  '/urs/local/bin/chromedriver'

# @pytest.fixture
# def driver(request):
#     wd = webdriver.Chrome(r'C:\Users\a.kosich\chromedriver.exe')
#     request.addfinalizer(wd.quit)
#     return wd
#
#
# def test_ex(driver):
#     driver.get("https://www.google.com/")
#     driver.find_element_by_name("q").send_keys("selenium")
#     driver.implicitly_wait(60)
#     driver.find_element_by_name("btnK").click()
#     WebDriverWait(driver, 100).until(EC.title_is("selenium - Поиск в Google"))
