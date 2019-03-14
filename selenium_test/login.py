# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time


@pytest.fixture
def driver(request):
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    firefox_capabilities['binary'] = '/usr/bin/firefox'
    firefox_capabilities['loggingPrefs'] = {'browser': 'ALL'}
    driver = webdriver.Firefox(capabilities=firefox_capabilities)
    driver.implicitly_wait(60)
    request.addfinalizer(driver.quit)
    # chrome_capabilities = DesiredCapabilities.CHROME
    # chrome_capabilities['loggingPrefs'] = { 'browser':'ALL' }
    # driver = webdriver.Chrome(desired_capabilities=chrome_capabilities)
    return driver


def test_login(driver):
    driver.get("http://localhost/litecart/public_html/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
