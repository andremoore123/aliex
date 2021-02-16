from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import timeit
import os
import random
from selenium.webdriver.chrome.options import Options
import random
from log import *
from faker import Faker

fake = Faker()
opts = Options()
email = pd.read_csv('baru.csv')   
os.system("clear")
for i in email.loc[0:,'email']:
    for x in email.loc[0:'password']:
        opts.add_argument('--disable-blink-features=AutomationControlled')
        browser = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=opts)
        logger.info("[*] Open link account settings")
        browser.get('https://login.aliexpress.com/express/buyer_login_new.htm')


        element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/section/div/div[2]/a')))
        element.click()
        # wait(browser,15).until(EC.new_window_is_opened(browser.window_handles))

        browser.switch_to.window(browser.window_handles[1])

        logger.info("[*] Login google")
        # enter email and password
        def email1():
            global element
            element = wait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#identifierId')))
        def entar_email():
            global element
            try:
                email1()
            except:
                browser.refresh()
                email1()
            else:
                element.send_keys(f"{i}@mskuwe.my.id")
                logger.info("[*] Enter email")
                element = wait(browser,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#identifierNext > div > button > div.VfPpkd-RLmnJb')))
                element.click()


            try:    
                element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
                element.send_keys("haha1234")
                logger.info("[*] Enter password")
                try:
                    logger.info("[*] Checking if back to google login")
                    entar_email()   
                except:
                    logger.info("[*] PASS!!!")
                    pass
            except Exception as e:
                sleep(2)
                print(e)
            else:   
                element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
                element.send_keys(Keys.ENTER)
                pass
        entar_email()
        # for gsuite only
        try:
            element = wait(browser,3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accept')))
        except:
            logger.info("[*] Skip gsuite authentication")    
        else:
            element.click()

        browser.switch_to.window(browser.window_handles[0])


        browser.get("https://accounts.aliexpress.com/user/organization/manage_person_profile.htm")
        try:
            wait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'fm-sns-item.google'))).click()
            logger.info("[*] Checking if back to login page")
        except:
            logger.info("[*] Pass!")
            pass    
        try:
            logger.info("[*] Checking the page full loaded")
            element = wait(browser,2).until(EC.presence_of_element_located((By.CLASS_NAME, 'right-cart-icon')))
        except:
            logger.info("[*] Pass!")
            pass
        browser.get("https://accounts.aliexpress.com/user/organization/manage_person_profile.htm")

        try:
            wait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'fm-sns-item.google')))
        except:
            browser.get("https://accounts.aliexpress.com/user/organization/manage_person_profile.htm")

        wait(browser,40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#preview-form > tbody > tr:nth-child(10) > td > a"))).click()
        name = list(fake.name().split())

        logger.info("[*] Entering name")
        element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#GroupListForm > table > tbody > tr:nth-child(1) > td > div:nth-child(1) > input")))
        element.clear()
        element.send_keys(f"{name[0]}")

        element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#GroupListForm > table > tbody > tr:nth-child(1) > td > div:nth-child(2) > input")))
        element.clear()
        element.send_keys(f"{name[1]}")

        random1 = ("#mr", "#ms")
        wait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"{random.choice(random1)}"))).click()
        logger.info("[*] Entering adddress")

        
        logger.info("[*] Entering city")
        city = ("pekanbaru","jakarta","dumai","duri")
        element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#GroupListForm > table > tbody > tr:nth-child(5) > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]")))
        element.clear()
        element.send_keys(f"{random.choice(city)}")
        logger.info("[*] Entering zip code")
        element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#GroupListForm > table > tbody > tr:nth-child(5) > td > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type=text]")))
        element.clear()
        element.send_keys(f"{random.randrange(1, 10**3):05}")
        logger.info("[*] Entering phone number")
        element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#GroupListForm > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(2) > input[type=text]")))
        element.clear()
        element.send_keys(f"{random.randrange(1, 10**3):03}")

        element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#GroupListForm > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(3) > input[type=text]")))
        element.clear()
        element.send_keys(f"{random.randrange(1, 10**3):08}")
        element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#GroupListForm > table > tbody > tr:nth-child(5) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]")))
        element.clear()
        element.send_keys(f"{fake.address()}")

        logger.info(f"[*] {i}mskuwe.my.id DONE!!")
        f = open('email.dat','w')
        f.write(str(f"{i}mskuwe.my.id DONE!!"))
        f.close 
        browser.quit()
        print()