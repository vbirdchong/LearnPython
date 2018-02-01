#! python3

import requests
from bs4 import BeautifulSoup
import sys

USAGE_INFO = '''
Usage: python Weather.py [city_name]
 e.g.: python Weather.py hangzhou'''

WEATHER_URL = 'http://tianqi.com/hangzhou/7'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}
PROXY = {'http': 'http://10.144.1.10:8080'}

def get_soup_from_link(url):
    req = requests.get(url, headers=HEADERS, proxies=PROXY, timeout=5)
    return BeautifulSoup(req.text)

def get_weather_report_list(weather_info):
    weather_report_list = []

    for group in weather_info:
        detail_info = {}
        txt = group.find_all(class_='txt')
        detail_info['date'] = group.find('dl').get_text()
        detail_info['description'] = group.find(class_='temp').get_text()
        detail_info['temperature'] = txt[0].get_text()
        detail_info['wind'] = txt[1].get_text()
        
        weather_report_list.append(detail_info)

    return weather_report_list

def print_day_weather(weather_list, city):
    print('City: ' + city)
    for weather in weather_list:
        print(weather['date'] + '\t' + weather['description'] + '\t' + weather['temperature'] + '\t' + weather['wind'])

def main():
    print(sys.argv)

    city = 'hangzhou'
    if len(sys.argv) == 1:
        city = 'hangzhou'
    elif len(sys.argv) == 2:
        city = sys.argv[1].lower()
    else:
        print(USAGE_INFO)
        return
    
    weather_url = 'http://tianqi.com/' + city + '/7'
    soup = get_soup_from_link(weather_url)
    weather_table_day7 = soup.find_all(class_='table_day7')
    weather_report_list = get_weather_report_list(weather_table_day7)
    print_day_weather(weather_report_list, city)

if __name__ == '__main__':
    main()
