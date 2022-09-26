from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_argument('--headless')
options.add_argument('--disable-extensions')
options.add_argument('--incognito')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
# options.add_argument(f'user-agent={ua}')
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')

driver = webdriver.Chrome(chrome_options=options)


driver.get("https://web.telegram.org/k/")
print("Waiting")
time.sleep(5)

# click on login button
login = driver.find_element(By.XPATH, '//div[@class="c-ripple"]')
print(login)
print("Login")
login.click()
time.sleep(5)

# enter number
number = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]')
print(number)
print("number")
time.sleep(2)
number.click()
print("Clicked")
time.sleep(2)
number.send_keys(Keys.BACK_SPACE)
number.send_keys(Keys.BACK_SPACE)
print("Sending Key")
number.send_keys("923117039097")

print("Cleared")

# number.send_keys(Keys.ENTER)
