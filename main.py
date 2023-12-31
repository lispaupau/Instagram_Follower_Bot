import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
import os

load_dotenv()

LOGIN = os.environ.get('login')
PASS = os.environ.get('pass')
SIMILAR_ACCOUNT = 'yumos_13'


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get(url='https://www.instagram.com/')
        time.sleep(2)
        enter_login = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        enter_login.send_keys(LOGIN, Keys.TAB)

        enter_pass = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        enter_pass.send_keys(PASS, Keys.ENTER)

        time.sleep(10)
        self.driver.find_element(By.XPATH, value='//button[contains(text(), "Не сейчас")]').click()

    def find_followers(self):
        self.driver.get(url=f'https://www.instagram.com/{SIMILAR_ACCOUNT}/followers')

        time.sleep(5)
        modal_xpath = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
        modal = self.driver.find_element(By.XPATH, value=modal_xpath)

        for i in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='//button[contains(text(), "Отмена")]')
                cancel_button.click()


inst_follows = InstaFollower()
inst_follows.login()
inst_follows.find_followers()
inst_follows.follow()
