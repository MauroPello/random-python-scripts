from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from datetime import datetime
from secret import credentials

otp = str(input("Enter OTP code: "))

if not len(otp) == 8:
    quit()

driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
driver.get("https://ihbnext.cedacri.it/home-banking-ng/public/login/?abi=05824&codiceProdotto=default&lang=it&codiceMyBank=undefined")

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@id="username"]')))
element.send_keys(credentials[0])

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@id="password"]')))
element.send_keys(credentials[1])

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/hbng-pre-cage-component/ui-view[2]/hbng-login-cage-component/div/div/ui-view[2]/hbng-login-component/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div[3]/button')))
ActionChains(driver).click(element).perform()

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp"]')))
element.send_keys(otp)

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-full-submit"]')))
ActionChains(driver).click(element).perform()

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'text.c-chart__value')))
current_balance = int(element.text.replace(" €", "").replace(".", "").replace(",", ""))

file = open("data_files/saldo.txt", "r+")

if not file.readable():
    file.close()
    print("File not readable")
    quit()

if not file.writable():
    file.close()
    print("File not writable")
    quit()

lines = file.readlines()
lines.reverse()

print("Last 10 balances check:")
for i in range(10):
    current_line = lines[i].replace("\n", "").split(";")
    print(str(i + 1) + "° last balance check (" + current_line[0] + ") was of: " + str(int(current_line[1]) / 100) + " €.")

#current date and time
now = datetime.now()
file.write(now.strftime("%H:%M:%S %d/%m/%Y") + ";" + str(current_balance) + "\n")

file.close()
driver.quit()
