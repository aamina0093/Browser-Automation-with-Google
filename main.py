from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# this code manually adds chrome driver
s = Service('C:\BrowserDrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)

countries = ['US', 'India', 'Belgium', 'Japan', 'Mexico']

for country in countries:
    driver.get('https://www.google.com/')
    query = 'When is independence day for ' + country + '?'

    # Locate the search input field by name 'q'
    text_field = driver.find_element(By.NAME, value='q')
    text_field.clear()  # Clear any existing text in the field
    text_field.send_keys(query)
    text_field.submit()

    time.sleep(2)
    result = driver.find_element(by=By.XPATH, value="//textarea[@id='APjFqb']")
    # rdate = driver.find_element(by=By.XPATH, value="//div[@class='Z0LcW t2b5Cf']")
    # print(f"Independence day for {country}: {result.}")
    time.sleep(2)
# Close the browser when done
driver.quit()
