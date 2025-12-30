from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep

import pytest


def test_navigation_and_titles(driver):
    title1 = driver.title
    print(f"\nTitle 1 (start): {title1}")
    sleep(5) 
    driver.get("https://www.google.com/")
    title2 = driver.title
    print(f"Title 2 : {title2}")
    sleep(5) 
    driver.back()
    title3 = driver.title
    print(f"Title 3 (back): {title3}")
    sleep(5) 
    driver.forward()
    title4 = driver.title
    print(f"Title 4 (forward): {title4}")
    sleep(5) 
    assert title1
    assert title2
    assert title3
    assert title4
