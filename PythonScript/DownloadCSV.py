#! python3

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

USAGE_INFO = '''
Usage: this script not implete at present'''

file_url = r'http://10.140.23.250:8080/job/MACAnalyzeServer/5941/AnalyzeRepor/SourceData/UserData/BTS886_2237_ttiTraceHb.dat.csv'
url = r'http://10.140.23.250:8080/job/MACAnalyzeServer/5941/AnalyzeRepor'
test_url = r'https://sites.google.com/a/chromium.org/chromedriver/getting-started'
baidu_url = r'http://www.baidu.com'


def main():
    driver = webdriver.Chrome(r'D:\LearnPython\PythonScript\chromedriver.exe')
    driver.get(url)
    time.sleep(2)
    # print(driver.page_source)
    soup = BeautifulSoup(driver.page_source)
    # print(soup.prettify())

    try:
        main_tab = driver.find_element_by_id('tab1').click()
        driver.switch_to_frame('myframe')
        analyzed_result_element = driver.find_element_by_link_text('BTS886_223A_ttiTraceHb_2.dat.csv')
        print(analyzed_result_element)
    except NoSuchElementException:
        print('Not find this element')
    
    input()
    driver.quit()
    # req = requests.get(file_url)
    # with open("test.csv", "wb") as test_file:
    #     test_file.write(req.content)

if __name__ == '__main__':
    main()
