from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service = Service(executable_path='C:\\Downloads\\chromedriver-win64\\chromedriver.exe')

service = Service(executable_path='usr/bin/chromedriver')


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(options=options)





