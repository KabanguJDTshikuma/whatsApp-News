from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from time import sleep

browser = webdriver.Firefox()
browser.get('https://web.whatsapp.com/')
print('Scan and get started')
#sleep(10)
input('Enter anything after scanning QR code')
# a = browser.find_element_by_class_name("_3NWy8").text
# r = browser.find_element_by_class_name("_1ZMSM").text
names = browser.find_elements_by_xpath('//div[@class = "_3H4MS"]')
msgs = browser.find_elements_by_xpath('//div[@class = "_2Bw3Q"]')

def sendNews():
    count = 0
    for msg in msgs:
        count += 1
        message = msg.text
        if message.lower() == "news":
            news5 = getNews()
            msg.click()
            text_bot = browser.find_elements_by_class_name("_3u328")
            response = "Hi " + names[count-1].text + "\n"
            text_bot[0].send_keys(response)
            for n in news5:
                text_bot[0].send_keys(news5[n] + '\n' + n + '\n')
                #text_bot[0].send_keys('\n')
                #text_bot[0].send_keys(news5[n])

            button = browser.find_element_by_class_name("_3M-N-")
            return button.click()
        


def getNews():
    url = "https://www.news24.com/TopStories"
    soup = BeautifulSoup(requests.get(url).content)
    articles = soup.find_all('h4', class_='bold')
    #news = [i.find('a').text for i in articles[:5]]
    #links = []
    news = {}
    for i in articles[:5]:
        link = i.find('a').get('href')
        # links.append(requests.get("http://thelink.la/api-shorten.php?url="+link).content.decode())
        news[requests.get("http://thelink.la/api-shorten.php?url="+link).content.decode()] = i.find('a').text[:100]
    return news

print(sendNews())