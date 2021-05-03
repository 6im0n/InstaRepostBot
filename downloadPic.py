from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from bs4 import BeautifulSoup
#import urllib.request
import json
from selenium.common.exceptions import NoSuchElementException
import re
#import requests
import time
import random
import os
import io
from PIL import Image
import hashlib
import shutil 
import psycopg2
import string
from instascrape import *
from post_to_account import postToAccount
from config import *
class thief:
    def __init__(self):
        print("stating session....")
        self.path = Picture_path
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opts)
        #open databasewebdriver.Firefox(firefox_options=opts)
        self.db = psycopg2.connect(database=databaseName,user=db_user,password=passwordDataBase,host="127.0.0.1",port="5432")
        self.cursor = self.db.cursor()
    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(7)
        coockie_button = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/button[1]")
        #coockie_button = self.driver.find_element_by_class_name("aOOlW  bIiDR  ")
        coockie_button.click()
        time.sleep(5)
        username_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        username_input.send_keys(username)
        time.sleep(5)
        password_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password_input.send_keys(password)
        time.sleep(5)
        login_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
        login_button.click()
        time.sleep(5)
        #ui.WebDriverWait(self.driver, 10).until(self.driver.find_element_by_xpath('//button[text()="Not Now"]')).click()
        #time.sleep(10)
        
    def downloadInstagramPics(self):

        number_photos = int(2)
        #self.driver.get("https://www.instagram.com/explore/") #explore page
        self.driver.get("https://www.instagram.com/explore/tags/PLACE you tage here/")

        for i in range(1,number_photos):

            #create random Id
            time.sleep(5)
            letters = string.ascii_lowercase
            ID = ''.join(random.choice(letters) for i in range(1,12))

            #click second post
           #post = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/div/div[1]/div[3]") #uncomment for explore tag
            post = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[3]") #comment for explore page
            ActionChains(self.driver).move_to_element(post).click().perform()
            time.sleep(5)

            #get current url and current url content
            current_Url = self.driver.current_url
            time.sleep(5)
            print(current_Url)
            imageScraping = Post(current_Url)
            headers = {
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
                "cookie": "sessionid="+self.driver.session_id+";"
            } 
            self.driver.close()
            imageScraping.scrape(headers=headers)
            print(imageScraping['display_url'])

            #get img url
            time.sleep(5)
            complete_url = imageScraping['display_url']

            #check if is video or not
            video_bool = str(imageScraping['is_video'])
            print(video_bool)
            time.sleep(10)

            #download picture
            if video_bool == "False":

                #get owner of post
                time.sleep(10)
                complete_username = str(imageScraping['username'])
                print("username: "+complete_username)

                #download picture
                r = requests.get(complete_url)
                os.chdir(self.path)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open("instagramSample.jpeg",'wb') as f:
                        f.write(r.content)
                        os.rename("instagramSample.jpeg",ID+".jpeg")
                        address = self.path + ID + ".jpeg"

                    #store it into a database (postgresql)
                    ID = "'" + ID + "'"
                    address = "'"+address+"'"
                    NOTPOSTED = "'NOTPOSTED'"
                    complete_username = "'"+complete_username+"'"
                    print("ID: "+ ID)
                    print("path: "+address)
                    print("status: " + NOTPOSTED)
                    self.cursor.execute("INSERT INTO photos_instagram (id,path,status,owner) \
      VALUES ({},{},{},{});".format(ID,address,NOTPOSTED,complete_username))
            else:
                print("is_video:true")
                pass
            
            #time.sleep(40)

            #go to next post
            #next_post = self.driver.find_element_by_xpath("/html/body/div[4]div[1]/div/div/a[2]")
            #next_post.click()                   
            time.sleep(10)

        self.db.commit()
        self.db.close()



bot = thief()
bot.login()
bot.downloadInstagramPics()
postToAccount()
