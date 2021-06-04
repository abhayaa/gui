import requests, selenium, time

import sqlite3, threading

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

# class element_has_non_empty_value(object):
#     def __init__ (self, locator):
#         self.locator = locator

#     def __call__(self, driver):
#         try:
#             element = EC._find_element(driver, self.locator).text
#             return element != ""
#         except StaleElementReferenceException:
#             return False

# def login_gmail():
#     option = webdriver.ChromeOptions()
#     option.add_argument('--disable-blink-features=AutomationControlled') 
#     driver.get('https://stackoverflow.com/users/login')
#     driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
#     time.sleep(1)

#     username = driver.find_element_by_xpath('//*[@id="identifierId"]')
#     username.send_keys(email)

#     driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()

   

def do_stuff(username, password):
    driver = webdriver.Chrome(executable_path='chromedriver')
    email = username
    password = password

    option = webdriver.ChromeOptions()
    option.add_argument('--disable-blink-features=AutomationControlled')    
    driver.maximize_window()
    driver.get('https://www.newegg.com/')
    driver.find_element_by_xpath('//*[@id="app"]/header/div[1]/div[4]/div[1]/div[1]/a/div[2]').click()
    driver.find_element_by_xpath('//*[@id="labeled-input-signEmail"]').click()
    driver.find_element_by_xpath('//*[@id="labeled-input-signEmail"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
    driver.implicitly_wait(5)
    
    while True:
        element = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[3]/form/div/div[3]/div/input[6]')
        text = element.get_attribute("value")
        if text == "":
            print("please enter code for " + email)
            time.sleep(2)
        else:
            print("Filled")
            break;
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
    time.sleep(2)
    driver.get('https://www.newegg.com/product-shuffle')

    time.sleep(3)

    for i in range(2,9):
        index = str(i)
        # '//*[@id="ItemInformation_Position"]/div[2]/div[3]/div[1]/div'
        link = '\'//*[@id="ItemInformation_Position"]/div[2]/div[3]/div[' + index + ']/div\''
        print(link)
        e = driver.find_element_by_xpath(link)
        actions = ActionChains(driver)
        actions.click(on_element = e)
        actions.perform()

        thread.join()
        driver.quit()
    
    
    '//*[@id="ItemInformation_Position"]/div[2]/div[3]/div[2]/div'
    '//*[@id="ItemInformation_Position"]/div[2]/div[3]/div[1]/div'
    '//*[@id="ItemInformation_Position"]/div[2]/div[3]/div[2]/div'

def run_checkout():
    con = sqlite3.connect('store.db')
    cur = con.cursor()
    
    accounts = []
    with con:
        cur.execute('SELECT * FROM accounts;')
        accounts = cur.fetchall()

    for account in accounts: 
        username = account[0]
        password = account[1]
        t1 = threading.Thread(target=do_stuff, args=(username, password))
        t1.start()
        
