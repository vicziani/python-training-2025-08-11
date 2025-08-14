from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.find_element(By.ID, "my-text-id").send_keys("Hello, Selenium!")

driver.find_element(By.TAG_NAME, "button").click()

sleep(2)
