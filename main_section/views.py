from django.shortcuts import render
from django.http import HttpResponse

from bs4 import BeautifulSoup
import requests
import re
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque
import time



def home(request):
    return render(request, 'main_section/index.html', {'page_title': "Home"})


#def email_scraper_bot_on_google(request):
#    return render(request, 'main_section/email-scraper-bot-on-google.html', {'page_title': 'Email Scraper on Google'})


"""
def search_bot_on_google(request):
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

    entered_phrase = request.GET['link'].replace(' ', '+') or 'google'

    emails = []
    possible_emails = []

    link_extensions = ['', 'contact', 'contact-us', 'contact.html', 'contact-us.html']
    #start_count = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120', '130', '140']
    start_count = ['0', '10', '20', '30', '40']

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regex2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    for num in start_count:
        source = requests.get("https://www.google.com/search?q=" + entered_phrase + "&start=" + num, headers=headers)
        soup = BeautifulSoup(source.text, 'lxml')
        parentElement = soup.findAll("div", {"class": "yuRUbf"})
        for element in parentElement:
            elementList = element.find("a")
            website = elementList.get("href")
            
            for extension in link_extensions:
                try:
                    website_source = requests.get(website + extension, timeout=10)
                    website_soup = BeautifulSoup(website_source.text, 'lxml')
                    find_emails = soup.body.findAll(text=re.compile('@'))
                    for email in find_emails:
                        if(re.search(regex,email) or re.search(regex2, email)):  
                            if email not in sent_emails:
                                emails.append(email)
                        else:
                            if len(email) <= 160:
                                possible_emails.append(email)
                except:
                    pass

    


    entered_phrase = request.GET['link'].replace(' ', '+') or 'google'
    google_pages = request.GET['page'] or 1
    websites = []
    page_title = "Email Scraper on Google"

    pages = range(0, int(google_pages)*10, 10)

    emails = []
    possible_emails = []
    start_count = []

    for x in pages:
        start_count.append(str(x))

    link_extensions = ['', 'contact', 'contact-us', '/contact', '/contact-us']
    #start_count = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120', '130', '140']

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regex2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    #PATH = "C:\Program Files (x86)\chromedriver.exe"
    #GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    #GOOGLE_CHROME_PATH = '/app/.apt/opt/google/chrome/google-chrome'
    #CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')

    driver = webdriver.Chrome(executable_path=str(os.environ.get('CHROMEDRIVER_PATH')), chrome_options=chrome_options)

    start_time = time.time() + 10

    while time.time() < start_time:
        for num in start_count:
            driver.get("https://www.google.com/search?q=" + entered_phrase + "&start=" + num)
            driver.implicitly_wait(5)
            parentElement = driver.find_elements_by_class_name("yuRUbf")
            for element in parentElement:
                elementList = element.find_element_by_tag_name("a")
                website = elementList.get_attribute("href")
                
                for extension in link_extensions:
                    try:
                        website_source = requests.get(website + extension, timeout=6)
                        if website_source.status_code == 200:
                            websites.append(website_source.url)
                            website_soup = BeautifulSoup(website_source.text, 'lxml')
                            find_emails = website_soup.body.findAll(text=re.compile('@'))
                            for email in find_emails:
                                if(re.search(regex,email) or re.search(regex2, email)):  
                                    if email not in emails:
                                        emails.append(email)
                                else:
                                    if len(email) <= 100:
                                        if email not in possible_emails:
                                            possible_emails.append(email)
                    except:
                        pass
    driver.quit()


    context = {
        'emails': emails,
        'possible_emails': possible_emails,
        'link': entered_phrase,
        'websites': websites,
        'page_title': page_title
    }
    return render(request, 'main_section/search-bot-on-google.html', context)
"""



def complete_website_email_scraper(request):
    return render(request, 'main_section/complete-website-email-scraper.html', {'page_title': 'Complete Website Email Scraper'})


def search_complete_website(request):
    emails = []
    possible_emails = []
    page_title = "Complete Website Email Scraper"

    url = str(request.GET['link']) or 'https://scrapethissite.com'

    new_urls = deque([url])
    processed_urls = set()
    local_urls = set()
    foreign_urls = set()
    broken_urls = set()

    a = 0

    processed_urls.add(url)
    processed_urls.add(url + '/contact')
    processed_urls.add(url + '/contact-us')

    start_time = time.time() + 15

    while time.time() < start_time:
        url = new_urls.popleft()
        processed_urls.add(url)
        try:
                response = requests.get(url, timeout=5)
        except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema, requests.exceptions.Timeout):
                broken_urls.add(url)
                pass
        try:
            parts = urlsplit(url)
            base = "{0.netloc}".format(parts)
            strip_base = base.replace("www.", "")
            base_url = "{0.scheme}://{0.netloc}".format(parts)
            path = url[:url.rfind('/')+1] if '/' in parts.path else url
        except:
            pass
        
        try:
            soup = BeautifulSoup(response.text, "lxml")
            for link in soup.find_all('a'):
                anchor = link.attrs["href"] if "href" in link.attrs else ''
                if anchor.startswith('/'):
                    local_link = base_url + anchor
                    local_urls.add(local_link)
                elif strip_base in anchor:
                    local_urls.add(anchor)
                elif not anchor.startswith('http'):
                    local_link = path + anchor
                    local_urls.add(local_link)
                else:
                    foreign_urls.add(anchor)
            for i in local_urls:
                if not i in new_urls and not i in processed_urls:
                    new_urls.append(i)
        except:
            pass
        a = a + 1
        if a >= 20:
            break

        try:
            for link in processed_urls:
                source = requests.get(link)
                if source.status_code == 200:
                    soup = BeautifulSoup(source.text, 'lxml')
                    find_emails = soup.findAll(text=re.compile('@'))

                    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                    regex2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
                    for email in find_emails:
                        if(re.search(regex, email) or re.search(regex2, email)):
                            if email not in emails:
                                    emails.append(email)  
                        else:
                            if len(email) <= 100:
                                if email not in possible_emails:
                                    possible_emails.append(email)
        except:
            pass

    context = {
        'emails': emails,
        'possible_emails': possible_emails,
        'link': link,
        'processed_urls': processed_urls,
        'page_title': page_title
    }

    return render(request, 'main_section/search-complete-website.html', context)


def search(request):
    emails = []
    possible_emails = []
    page_title = "Home"

    link = request.GET['link'] or 'https://google.com'

    start_time = time.time() + 20

    while time.time() < start_time:
        try:
            source = requests.get(link)
            soup = BeautifulSoup(source.text, 'lxml')
            find_emails = soup.body.findAll(text=re.compile('@'))

            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            regex2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
            for email in find_emails:
                if(re.search(regex, email) or re.search(regex2, email)):
                    if email not in emails:
                            emails.append(email)  
                else:
                    if len(email) <= 100:
                        possible_emails.append(email)
            break
        except:
            pass
    
    context = {
        'emails': emails,
        'possible_emails': possible_emails,
        'link': link,
        'page_title': page_title
    }
    return render(request, 'main_section/search.html', context)
