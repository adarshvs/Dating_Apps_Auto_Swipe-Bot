from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
from random import randint

class BumbleBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://bumble.com/app')

        sleep(4)
        print("Please log into your tinder account manually and provide necessary browser permissions.\n")
        print("Log in with mobile number is preferable. \n")
        print("Don't forget to maximize your browser or this script won't work.\n")
         
        user_input = input("have you logged in ? yes or no : ")
        
        if user_input == 'yes':
                moves = [Keys.LEFT, Keys.RIGHT, Keys.ESCAPE]
                while True:
                        sleep(randint(4,10))
                        bot.driver.find_element(By.CSS_SELECTOR, "body").send_keys(random.choice(moves))
                        #bot.driver.find_element_by_css_selector('body').send_keys(random.choice(moves))
        else:
                print('sorry i cannot help you if you do not login')


bot = BumbleBot()
bot.login()
