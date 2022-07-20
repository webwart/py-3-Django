from django.test import LiveServerTestCase
from selenium import webdriver
import time 

class Hosttest(LiveServerTestCase):

    def testhomepage(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000')
        assert "Home" in driver.title
        time.sleep(3)
        driver.quit()

    def testhomepageEdge(self):
        driver3 = webdriver.Edge()
        driver3.get('http://127.0.0.1:8000')
        assert "Home" in driver3.title
        time.sleep(3)
        driver3.quit()

    def testhomepageFire(self):
        driver2 = webdriver.Firefox()
        driver2.get('http://127.0.0.1:8000')
        assert "Home" in driver2.title
        time.sleep(3)
        driver2.quit()
