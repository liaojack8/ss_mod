import requests
import cloudscraper
import random
from bs4 import BeautifulSoup

def getLatestUAUrl():
    # req = requests.get('https://user-agents.net/applications/instagram-app/versions')
    # reqbs = BeautifulSoup(req.text, 'html5lib')
    file = open('example1.html', 'r')
    reqbs = BeautifulSoup(file.read(), 'html5lib')
    url = reqbs.find(class_='compact_list').find('li').find('a')['href'].strip()
    return f'https://user-agents.net{url}'
    
def getUA(link):
    # req = requests.get(link)
    # reqbs = BeautifulSoup(req.text, 'html5lib')
    file = open('example2.html', 'r')
    reqbs = BeautifulSoup(file.read(), 'html5lib')
    UAs = reqbs.find(class_='agents_list').find_all('li')
    UA = 'Moz'
    while(True):
        UA = random.choice(UAs).text
        if 'Android' in UA:
            break
    return UA

def getLatestIGVersion():
    # file = open('example3.html', 'r', encoding='utf-8')
    # reqbs = BeautifulSoup(file.read(), 'html5lib')
    scraper = cloudscraper.create_scraper()
    req = scraper.get('https://apkpure.com/instagram-android/com.instagram.android/versions')
    reqbs = BeautifulSoup(req.text, 'html5lib')
    VersionNumber = reqbs.find(class_='ver-item-n').contents[0].split('\n')[2].replace('                ','')
    return VersionNumber

def main():
    UAUrl = getLatestUAUrl()
    UA = getUA(UAUrl)
    VersionNumber = getLatestIGVersion()
    print(UA, VersionNumber)


if __name__ == '__main__':
    main()