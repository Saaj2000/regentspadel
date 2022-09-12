# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:49:15 2022

@author: Saajan
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]
username_email = ""
passw = ""

card = 
expiry = 
cvv = 
day = "Sun" #choose from Mon, Tue, Wed, Thu, Fri, Sat, Sun
bookingtime= "0900" #set in 24hr hh00 format, denotes start time for booking

driver = webdriver.Chrome(r"C:\Users\Saajan Shah\Desktop\chromedriver.exe") #set location of chromedriver.exe

driver.get("https://www.openplay.co.uk/booking/place/154")

driver.find_element_by_xpath('//a[@href="?mode=nonMember"]').click()
dropdown = driver.find_element_by_name("use")
dd = Select(dropdown)
dd.select_by_index(1)
datedrop = driver.find_element_by_name("date")
dd2 = Select(datedrop)
elements = dd2.options
dates = [x.text for x in elements]
days = [x[0:3] for x in dates]
index = indices(days,day)
dd2.select_by_index(index[-1])
timexpath = "//a[@id='booklink-3530-" + bookingtime + "']"
a = driver.find_element_by_xpath(timexpath).get_attribute("href")

driver.get(a)

driver.find_element_by_xpath("//a[@id='pricingOption']").click()
driver.find_element_by_xpath("//a[@id='cart-continue']").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a").click()
wait = WebDriverWait(driver,5)
username = wait.until(EC.element_to_be_clickable((By.ID, "loginEmail")))
email = driver.find_element_by_xpath("//*[@id='loginEmail']")
email.send_keys(username_email)
password = driver.find_element_by_xpath("//*[@id='loginPassword']")
password.send_keys(passw)
driver.find_element_by_xpath("//*[@id='loginBtn']").click()
driver.find_element_by_xpath("//*[@id='submit']").click()
driver.find_element_by_xpath("//*[@id='confirm-checkbox']").click()
driver.find_element_by_xpath("//*[@id='complete-order']").click()
driver.switch_to.frame("smallModal-frame")
driver.switch_to.frame(0)
driver.find_element_by_xpath("//*[@id='root']/form/span[2]/div/div[2]/span/input").send_keys(card)
driver.switch_to.default_content()
driver.switch_to.frame("smallModal-frame")
driver.switch_to.frame(1)
driver.find_element_by_xpath("//*[@id='root']/form/span[2]/span/input").send_keys(expiry)
driver.switch_to.default_content()
driver.switch_to.frame("smallModal-frame")
driver.switch_to.frame(2)
driver.find_element_by_xpath("//*[@id='root']/form/span[2]/span/input").send_keys(cvv)
driver.switch_to.default_content()
driver.switch_to.frame("smallModal-frame")
username = wait.until(EC.element_to_be_clickable((By.ID, "submit-card")))
driver.find_element_by_xpath('//*[@id="submit-card"]').click()


