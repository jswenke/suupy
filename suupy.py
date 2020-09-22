from tkinter import *

from tkinter import messagebox

import pyautogui

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

from tkinter import messagebox

import unittest

import time

from datetime import datetime

####################################################################

def refresh_page():
    
    root = Tk()
    
    driver = unittest.TestCase.driver
    driver.refresh()
    Label(root, text=datetime.now()).grid(row=15, sticky=W+E)

    root.mainloop()
    
####################################################################

def run_bot():
    
    item_select(entry_1.get())                                              ##input item name (exactly)
    size_select(entry_2.get())                                              ##input size
    masterFuncName('commit', 0, 0)
    masterFuncXpath('//*[@id="cart"]/a[2]', time.sleep(.2))
    masterFuncName('order[billing_name]', 0, entry_3.get())                 ##input name
    masterFuncName('order[email]', 0, entry_4.get())                        ##input email
    masterFuncName('order[tel]', 0, entry_5.get())                          ##input phone number
    masterFuncName('order[billing_address]', 0, entry_6.get())              ##input shipping address
    masterFuncName('order[billing_zip]', 0, entry_7.get())                  ##input zip
    
    masterCardNo('credit_card[cnb]', 0, '4060687037130179')  
    ##pyautogui.typewrite(entry_8.get(), interval=.1)                         ##input card no.
    
    
    ccExpMo()
    ccExpYe()
    masterFuncName('credit_card[vval]', 0, entry_9.get())                   ##input security code
    masterFuncXpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins',0)

####################################################################
    
def masterCardNo(locateSelf, optionalTimeSleepHere, sendKeys):

    driver = unittest.TestCase.driver
    inputKeys = sendKeys
    
    locateElement = locateSelf
    elementLocation = WebDriverWait(driver, 4).until(lambda driver: driver.find_element_by_name(locateElement))
    optionalTimeSleepHere
    elementLocation.click()

####################################################################


def setUp():
    unittest.TestCase.driver = webdriver.Chrome("/Users/USERNAMEHERE/Desktop/chromedriver.exe")
    unittest.TestCase.driver.get("http://www.supremenewyork.com/shop/all/accessories")

####################################################################
    
def category_find():

    driver = unittest.TestCase.driver
        
    itemCSS   = '//*[@id="nav-categories"]/li[11]/a'
    itemElement = WebDriverWait(driver,.5).until(lambda driver: driver.find_element_by_xpath(itemCSS))                   

    itemElement.click()
    WebDriverWait(driver, .5).until(lambda driver: driver.find_element_by_xpath(itemCSS))

####################################################################

def item_select(itemInput):

    driver = unittest.TestCase.driver
 
    ##itemSelectName    = 'Supreme®/Hanes® Tagless Tees (3 Pack)'
    
    itemSelectName = itemInput
    itemSelectElement = [];
    itemSelectElement = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_link_text(itemSelectName))          
    itemSelectElement.click()

####################################################################

def size_select(sizeInput):

    driver = unittest.TestCase.driver

    itemSizeChoice  = sizeInput
    itemSelectSize  = 's'
    itemSelectSize = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_name(itemSelectSize))
    select           = Select(itemSelectSize)
    select.select_by_visible_text(itemSizeChoice)  

####################################################################

def masterFuncXpath(locateSelf, optionalTimeSleepHere):

    driver = unittest.TestCase.driver

    locateElement = locateSelf
    elementLocation = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_xpath(locateElement))
    optionalTimeSleepHere
    elementLocation.click()

####################################################################

def masterFuncCSS(locateSelf, optionalTimeSleepHere):

    driver = unittest.TestCase.driver

    locateElement = locateSelf
    elementLocation = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(locateElement))
    optionalTimeSleepHere
    elementLocation.click()

####################################################################

def masterFuncName(locateSelf, optionalTimeSleepHere, sendKeys):

    driver = unittest.TestCase.driver
    inputKeys = sendKeys
    
    locateElement = locateSelf
    elementLocation = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_name(locateElement))
    optionalTimeSleepHere
    elementLocation.click()
    elementLocation.send_keys(inputKeys)

    
####################################################################

def ccExpMo():

    driver = unittest.TestCase.driver

    hoodieSizeChoice  = '01'
    hoodieSelectSize  = 'credit_card[month]'
    hoodieSelectSize = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_name(hoodieSelectSize))
    select           = Select(hoodieSelectSize)
    select.select_by_visible_text("01")  
 
####################################################################

def ccExpYe():

    driver = unittest.TestCase.driver

    hoodieSizeChoice  = '2019'
    hoodieSelectSize  = 'credit_card[year]'
    hoodieSelectSize = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_name(hoodieSelectSize))
    select           = Select(hoodieSelectSize)
    select.select_by_visible_text("2019")  
 
####################################################################

def menu_setup():

    root = Tk()
    root.title('Supreme Bot v0.1 by vid_')
    
    global entry_1
    entry_1 = Entry(root)
    global entry_2
    entry_2 = Entry(root)
    global entry_3
    entry_3 = Entry(root)
    global entry_4
    entry_4 = Entry(root)
    global entry_5
    entry_5 = Entry(root)
    global entry_6
    entry_6 = Entry(root)
    global entry_7
    entry_7 = Entry(root)
    global entry_8
    entry_8 = Entry(root)
    global entry_9
    entry_9 = Entry(root)

    Label(root, text='Item name').grid(row=0, sticky=E)
    Label(root, text='Size').grid(row=1, sticky=E)
    Label(root, text='Billing name').grid(row=2, sticky=E)
    Label(root, text='Email').grid(row=3, sticky=E)
    Label(root, text='Phone number').grid(row=4, sticky=E)
    Label(root, text='Shipping address').grid(row=5, sticky=E)
    Label(root, text='Zip').grid(row=6, sticky=E)
    Label(root, text='Card number').grid(row=7, sticky=E)
    Label(root, text='Security code').grid(row=8, sticky=E)

    Label(root, text=datetime.now()).grid(row=15, sticky=W+E)

    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    entry_3.grid(row=2, column=1)
    entry_4.grid(row=3, column=1)
    entry_5.grid(row=4, column=1)
    entry_6.grid(row=5, column=1)
    entry_7.grid(row=6, column=1)
    entry_8.grid(row=7, column=1)
    entry_9.grid(row=8, column=1)

    Button(root,text= 'Open webpage', command=setUp).grid(row=12, column=1, sticky=W+E, pady=5)
    Button(root,text= 'Refresh', command=refresh_page).grid(row=13, column=1, sticky=W+E, pady=5)
    Button(root,text= 'Run', command=run_bot).grid(row=14, column=1, sticky=W+E, pady=5)

    root.mainloop()

####################################################################

def login_menu_setup():
    
    login = Tk()
    login.title('Supreme Bot v0.1 by vid_ (Profile login)')
    mainframe = Frame(login)
    
    
    global entry_login
    entry_login = Entry(login)

    global entry_password
    entry_password = Entry(login)
    
    Label(login, text='Enter username and password or type "None" for both.').grid(row=0, column=1, sticky=E+W+N+S, pady=10)
    Label(login, text='Username:').grid(row=1, column=1, sticky=W)
    Label(login, text='Password:').grid(row=2, column=1, sticky=W)
    entry_login.grid(row=1, column=1)
    entry_password.grid(row=2, column=1)
    
    Button(login,text= 'Submit', command=menu_continue).grid(row=3, column=1, sticky=E+W+N+S, pady=10, padx=10)

    
    login.mainloop()

   
    
####################################################################

def menu_continue():
    if entry_login.get() == 'Jacob' and entry_password.get() == 'pass':
        menu_setup()    
    elif entry_login.get() == 'None' and entry_password.get() == 'None':
        menu_setup()
    else:
        messagebox.showerror('Error', 'Invalid username')
        
    
####################################################################




login_menu_setup()






















