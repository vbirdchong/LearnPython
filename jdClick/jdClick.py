#! /usr/bin/env python
# -*- coding=utf-8 -*-

from selenium import webdriver


def main():
    browser = webdriver.Chrome()
    print(type(browser))
    browser.get('https://sale.jd.com/act/ykY82hC5Gs3Sx4ew.html?cpdad=1DLSUE')
    try:
        elem = browser.find_element_by_css_selector('area[clstag="pageclick|keycount|UserDefine_19865271_1|0"]')
        # elem = browser.find_element_by_name('pageclick|keycount|UserDefine_21546861_2|0')
        print(type(elem))
        print(elem.tag_name)
        print(elem.get_attribute('href'))
        elem.click()
    except Exception as e:
        raise e

    browser.get(elem.get_attribute('href'))
    # clickLogin = browser.find_element_by_css_selector('a[clstag="pageclick|keycount|201607144|2"]')
    # elem.click()

    logIn = browser.find_element_by_css_selector('input[id="loginname"]')
    logIn.send_keys('cc.chong.chen@gmail.com')
    password = browser.find_element_by_css_selector('input[id="nloginpwd"]')
    password.send_keys('l6o2v0e806love')
    password.submit()


if __name__ == '__main__':
    main()
    raw_input()
