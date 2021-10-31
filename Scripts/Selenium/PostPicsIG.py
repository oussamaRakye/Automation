from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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