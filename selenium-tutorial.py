from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from requests import get

driver = webdriver.Chrome()

driver.get("https://www.rottentomatoes.com/")

search_form = driver.find_element_by_class_name("form-control")
search_form.send_keys("Fast and Furious")

button = driver.find_element_by_id("fullscreen-search-desktop-search-btn")
button.click()

html_soup = BeautifulSoup(driver.page_source, features="html.parser")
