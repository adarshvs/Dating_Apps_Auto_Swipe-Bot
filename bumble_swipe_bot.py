from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
from random import randint

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://bumble.com/get-started')

        sleep(4)
        print("Please log into your Tinder account manually and provide necessary browser permissions.\n")
        print("Log in with a mobile number is preferable.\n")
        print("Don't forget to maximize your browser or this script won't work.\n")

        user_input = input("Have you logged in? (yes or no): ")

        if user_input.lower() == 'yes':
            moves = [Keys.RIGHT, Keys.RIGHT, Keys.ESCAPE, Keys.RIGHT, Keys.RIGHT, Keys.LEFT]  # Reduce frequency of left button press
            while True:
                interval = randint(4, 15)
                sleep(interval)
                move = random.choice(moves)
                self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(move)
                print(f"Action performed: {move}, sleeping for {interval} seconds.")
                
                # Randomly reload the page
                if random.random() < 0.1:  # 10% chance to reload the page
                    print("Reloading page...")
                    self.driver.refresh()
                    sleep(randint(10, 20))  # Additional sleep after reloading
        else:
            print('Sorry, I cannot help you if you do not log in.')

bot = TinderBot()
bot.login()
