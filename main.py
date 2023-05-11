from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

P_DOWN = 2
P_UP = 1
EMAIL = "doniyke25@yahoo.com"
P_W = "Alanoddin.25"


class InternetSpeedTwitterBot():
    def __init__(self):
        self.P_DOWN = 0
        self.P_UP = 0
        self.driver = webdriver.Firefox()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go.send_keys(Keys.ENTER)
        time.sleep(5)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        self.P_DOWN = self.down.text
        self.P_UP = self.up.text

    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com/")
        login = self.driver.find_element(By.LINK_TEXT, "Log in")
        login.click()
        time.sleep(5)
        input_email = self.driver.find_element(By.TAG_NAME, 'input')
        input_email.send_keys(EMAIL)
        time.sleep(5)
        next = self.driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next.click()
        time.sleep(5)
        username = self.driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys("@donalbin")
        next_usernam = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        next_usernam.click()
        time.sleep(5)
        password_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_field.send_keys(P_W)
        time.sleep(5)
        login_final = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login_final.click()
        time.sleep(5)
        tweet = f" Yellow Dear MTN, your DownLoad speed ={self.P_DOWN} and Upload speed ={self.P_UP}. what are u supposed to provid us. \n\n  from internet webcrawler app"
        print(tweet)
        tweet_place = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div')
        tweet_place.send_keys(tweet)
        time.sleep(5)
        tweet_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()
        self.driver.quit()
bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()
