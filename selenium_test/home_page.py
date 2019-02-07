import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def driver(request):
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    wd = webdriver.Firefox(capabilities=caps)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("selenium")
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 10).until(EC.title_is("selenium - Поиск в Google"))
