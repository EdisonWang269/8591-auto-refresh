from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import os
import time

chromedriver_path = 'drivers\chromedriver.exe'

account = os.getenv('ACCOUNT')
password = os.getenv('PASSWORD')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
driver.get("https://www.8591.com.tw/user-login.html?aid=760")
driver.maximize_window()

account = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'accounts')))

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'pwd')))

account.clear()
account.send_keys(account)
password.clear()
password.send_keys(password)

login = driver.find_element(By.ID, 'send')
login.click()

time.sleep(1)

driver.get('https://www.8591.com.tw/userPublish-index.html')

refresh_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, '更新')))
refresh_btn.click()

send = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'j-p-ok')))
send.click()

driver.quit()
