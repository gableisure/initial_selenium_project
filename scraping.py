from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Scraping:

    def __init__(self):
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(options=options)
        self.browser.set_window_size(1024, 768)

    def run(self):
        print(f'\nExecutando scraping...')
        self.browser.get('https://www.linkedin.com/in/gabrielscientist/')

        sleep(10)

        self.browser.close()