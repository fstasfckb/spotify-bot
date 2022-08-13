import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from tkinter import Tk



def prepering():
    driver = webdriver.Chrome()
    driver.get('https://open.spotify.com/')
    time.sleep(1)
    btn = driver.find_element(By.ID , "onetrust-accept-btn-handler")
    btn.click()
    time.sleep(1)
    btn = driver.find_element(By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0")
    btn.click()

    time.sleep(1)

    username = "fstaswho@icloud.com"
    password = "defoxxxxxxx7"

    driver.find_element(By.ID , "login-username").send_keys(username)

    # найти поле ввода пароля и также вставить пароль
    driver.find_element(By.ID , "login-password").send_keys(password)

    btn = driver.find_element(By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0")
    btn.click()

    time.sleep(10)
    btn = driver.find_element(By.LINK_TEXT , "Поиск")
    btn.click()

    return driver

def listen(yoursong,driver):
    try :
        btn = driver.find_element(By.CLASS_NAME, "ZtY42R4YSo_W7VMeAg9m")
        btn.click()

        driver.find_element(By.CLASS_NAME , "Type__TypeElement-goli3j-0").send_keys(yoursong)

        btn = driver.find_element(By.CLASS_NAME , "g3Xinb8x23n81ejvS9Uj")
        btn.click()

        time.sleep(2)

        btn = driver.find_element(By.CLASS_NAME , "T0anrkk_QA4IAQL29get")
        btn.click()

        time.sleep(1)

        btn = driver.find_elements(By.CLASS_NAME , "QgtQw2NJz7giDZxap2BB")
        btn[1].click()

        btn = driver.find_elements(By.CLASS_NAME , "wC9sIed7pfp47wZbmU6m")
        btn[8].click()
        tk = Tk()
        return tk.clipboard_get()
    except:
        driver.find_element(By.CLASS_NAME , "Type__TypeElement-goli3j-0").send_keys(yoursong)

        btn = driver.find_element(By.CLASS_NAME , "g3Xinb8x23n81ejvS9Uj")
        btn.click()

        time.sleep(2)

        btn = driver.find_element(By.CLASS_NAME , "T0anrkk_QA4IAQL29get")
        btn.click()

        time.sleep(1)

        btn = driver.find_elements(By.CLASS_NAME , "QgtQw2NJz7giDZxap2BB")
        btn[1].click()

        btn = driver.find_elements(By.CLASS_NAME , "wC9sIed7pfp47wZbmU6m")
        btn[8].click()
        tk = Tk()
        return tk.clipboard_get()
