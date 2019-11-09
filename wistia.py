from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
from os.path import join, dirname
import urllib.request
import time
import config

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


if len(config.videos) <= 0:
    print('Error: There are no videos specified in config.videos')
    exit()

if len(config.qualities) <= 0:
    print('Error: There are no qualities specified in config.qualities')
    exit()

driver = webdriver.Chrome()

for video in config.videos:
    id = video['link'].split('"')[1].split('=')[1]

    driver.get('https://getvideo.at/en/')
    
    driver.find_element(By.ID, 'search-text').send_keys('https://fast.wistia.net/embed/iframe/' + id)

    driver.find_element(By.ID, 'search-button').click()

    time.sleep(3)
    
    for quality in config.qualities:
        test_xpath = "//*[contains(text(),'" + quality + "')]/parent::*"
        
        if check_exists_by_xpath(test_xpath):
            video_url = driver.find_element(By.XPATH, test_xpath).get_attribute("href")
            break
    
    if video_url == None:
        print('Error: From the qualities you specified, none were available for the video' + video.filename)

    if not os.path.exists(video['path']):
        os.makedirs(video['path'])

    urllib.request.urlretrieve(video_url, video['path'] + video['filename'] + '.mp4')
