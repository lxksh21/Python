from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os



class InstaBot:
    def __init__(self, usernm, passwrd):
        self.usernm = usernm
        self.passwrd = passwrd
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Firefox()
        self.login()



        time.sleep(3)

    def login(self):

        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(5)
        self.driver.find_element_by_name('username').send_keys(self.usernm)
        self.driver.find_element_by_name('password').send_keys(self.passwrd)
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(1)
    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url,user))

        time.sleep(3)

    def follow_user(self,user):
        self.nav_user(user)
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[contains(text(),"Follow")]').click()

        time.sleep(5)
    def unfollow_user(self,user):
        self.nav_user(user)

        time.sleep(3)

        self.driver.find_element_by_css_selector('.glyphsSpriteFriend_Follow').click()

        time.sleep(5)

        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
        time.sleep(5)








            






if __name__=='__main__':
    ig_bot = InstaBot('','') #add your username and password
    #ig_bot.nav_user('marshmellomusic')
    ig_bot.follow_user('marshmellomusic')
    ig_bot.unfollow_user('marshmellomusic')
