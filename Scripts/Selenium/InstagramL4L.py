from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get('https://www.selenium
# easy.com/test/basic-first-form-demo.html')
#
# messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
# messageField.send_keys("hello")
#
# showButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
# showButton.click()


driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')

wait = WebDriverWait(driver, 20)

#sleep(2)
print(driver.find_element_by_xpath('/html'))
emailField = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"loginForm\"]/div/div[1]/div/label/input")))
emailField.send_keys("oussama_rakye")

password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys("dof12ineT")

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login.click()

sleep(100)

#notification = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[3]/button[2]')))
#notification.click()

# Personal profile
#username = account.get_attribute('href')
driver.get('https://www.instagram.com/explore/tags/like4likes/')

sleep(5)
# Open first picture
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a"))).click()

# Like first picture
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/article/div/div[3]/section[1]/span[1]/button'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div/div/a'))).click()

while True:
    try:
        sleep(1)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/article/div/div[3]/section[1]/span[1]/button'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div/div/a[2]'))).click()
    except:
        pass

print('All liked')