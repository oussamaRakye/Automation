from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
#
# messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
# messageField.send_keys("hello")
#
# showButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
# showButton.click()


driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')

wait = WebDriverWait(driver, 10)

#sleep(2)
print(driver.find_element_by_xpath('/html'))
emailField = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")))
emailField.send_keys("osamarayke@gmail.com")

password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
password.send_keys("dof12ineT")

login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
login.click()

notification = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[3]/button[2]')))
notification.click()

# Personal profile
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a'))).click()
#username = account.get_attribute('href')

# Folowwers
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//body//div[contains(@class, 'v9tJq  VfzDr')]//ul//li[2]//a"))).click()

# First follower profile
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/ul/div/li/div/div[2]/div[1]/div/div/a'))).click()

# Open first picture
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//body//div[contains(@class,'_2z6nI')]//div//div//div[1]//div[1]//a[1]//div[1]//div[2]"))).click()

# Like first picture
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div/div/a'))).click()

while True:
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div/div/a[2]'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'))).click()
    except:
        break

print('All liked')