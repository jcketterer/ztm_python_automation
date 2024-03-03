# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# # service = Service(executable_path='C:\Downloads\chromedriver-win64\chromedriver.exe')

# service = Service(executable_path='usr/bin/chromedriver')


# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# chrome_browser = webdriver.Chrome(options=options)

# chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# assert 'Selenium Easy Demo' in chrome_browser.title

# button = chrome_browser.find_element(By.CLASS_NAME, 'btn btn-primary')

# print(button)


from selenium import webdriver
from selenium.webdriver.common.by import By

#The below 3 lines ignores the https://demo.seleniumeasy.com SSL cert in case it is missing. Making your output cleaner. It isn't necessary, but added it here for you just in case. 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("detach", True)

chrome_browser = webdriver.Chrome(options=options)
# chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# This solves the issue with the Popup for those that encounter it:
# chrome_browser.implicitly_wait(2)
# popup =chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()



user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')

# time.sleep(2)
assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button= chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
show_message_button.click()
assert 'Show Message' in chrome_browser.page_source

output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I AM EXTRA COOOOL' in output_message.text

# output_message = chrome_browser.find_element(By.ID, 'display')
# assert 'I AM EXTRA COOOOL' in output_message.text
#chrome_browser.quit()