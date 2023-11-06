from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
driver.get("https://app.erasmusplusols.eu/")
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'era-login')))
element.send_keys("INSERISCI EMAIL")
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'era-password')))
element.send_keys("INSERISCI PASSWORD")
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div/div/form/div[3]/button')))
ActionChains(driver).click(element).perform()

time.sleep(10)

# esempio link valido
# https://app.erasmusplusols.eu/platform/#/learning-path/mission/GIVE_DIRECTIONS_A1/lesson/EN_GB_A1_VOCABULARY_ASK_FOR_AND_GIVE_DIRECTIONS_IN_A_BUILDING/activity/EN_GB_A1_VOCABULARY_ASK_FOR_AND_GIVE_DIRECTIONS_IN_A_BUILDING_VOCABULARY_LIST_VOCABULARY/vocabulary-list/item/0
driver.get("INSERISCI LINK")

while True:
    time.sleep(120)

    try:
        # esempio funzionante con gli esercizi del vocabolario
        # preme quindi il pulsante vocabulary-list-activity-continue-button per andare alla voce dopo
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'vocabulary-list-activity-continue-button')))
        ActionChains(driver).click(element).perform()
    except TimeoutException:
        break


driver.quit()
