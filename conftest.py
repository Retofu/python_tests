from selenium import webdriver
import pytest
from time import sleep

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    yield chrome_driver