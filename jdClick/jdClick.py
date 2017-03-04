#! /usr/bin/env python
# -*- coding=utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    browser = webdriver.Chrome()
    browser.get('https://sale.jd.com/act/ykY82hC5Gs3Sx4ew.html?cpdad=1DLSUE')
    try:
        elem = browser.find_element_by_css_selector('area[clstag="pageclick|keycount|UserDefine_19865271_1|0"]')
        # elem = browser.find_element_by_name('pageclick|keycount|UserDefine_21546861_2|0')
        # print(type(elem))
        # print(elem.tag_name)
        # print(elem.get_attribute('href'))
        elem.click()
    except Exception as e:
        raise e

    browser.get(elem.get_attribute('href'))

    elem = browser.find_element_by_css_selector('a[clstag="pageclick|keycount|201607144|2"]')
    elem.click()
    wait = WebDriverWait(browser, 10)

    logIn = wait.until(EC.visibility_of_element_located((By.NAME, "loginname")))
    logIn.clear()
    logIn.send_keys('username')

    password = wait.until(EC.visibility_of_element_located((By.NAME, "nloginpwd")))
    password.clear()
    password.send_keys('password')
    password.submit()


    # logIn = browser.find_element_by_css_selector('input[id="loginname"]')
    # print(logIn.get_attribute('id'))
    # logIn.send_keys('cc.chong.chen@gmail.com')
    # password = browser.find_element_by_css_selector('input[id="nloginpwd"]')
    # password.send_keys('l6o2v0e806love')
    # password.submit()


if __name__ == '__main__':
    main()
    raw_input()
