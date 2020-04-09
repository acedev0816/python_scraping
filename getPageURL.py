import sys
import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

#delay time
wait_time = 5
#first run flag
flag = 0

driver = Chrome('.\\chromedriver.exe')

init_url = "https://app.plus500.com/trade/apple"

wait = WebDriverWait(driver,10)

url = init_url

driver.get(url)

#press demo
demo_button = driver.find_elements_by_id('demoMode')[0]
demo_button.click()

time.sleep(wait_time)

	#user
account = driver.find_elements_by_id('newUserCancel')[0]
account.click()

time.sleep(wait_time)
#log in
	#user email
u = driver.find_elements_by_id('email')[0]
u.send_keys('freelancer.bot9@gmail.com')

	#user pass
p = driver.find_elements_by_id('password')[0]
p.send_keys('lancbot9')
	#login
login = driver.find_elements_by_id('submitLogin')[0]
login.click()



time.sleep(10)
content = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div[1]")[0]
print (content.text.strip())

