from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

class WebDriver:

    def __init__(self):
        opt = Options()
        opt.set_preference("permissions.default.microphone", 1)
        opt.set_preference("permissions.default.camera", 1)
        self.__browser = webdriver.Firefox(executable_path=resource_path('.\\driver\\geckodriver.exe'), options=opt)
        self.__browser.get('https://meet.google.com/?authuser=0')
        sleep(3)
        
    def reset(self):
        self.__browser.get("https://meet.google.com/?authuser=0")
        sleep(3)

    def login(self, email, password):
        self.__browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div').click()
        sleep(1)
        self.__browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
        sleep(0.5)
        self.__browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(2)
        self.__browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        sleep(0.5)
        self.__browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(3)
        if self.__browser.current_url[0:23] != "https://meet.google.com":
            raise Exception("Failed to login!")

    def hasCode(self, code):
        self.__browser.get('https://meet.google.com/?authuser=0')
        sleep(3)
        origURL = self.__browser.current_url
        self.__browser.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div/div/div/div[1]').click()
        sleep(0.75)
        self.__browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input').send_keys(code)
        sleep(0.75)
        self.__browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/span/div/div[4]/div[2]/div').click()
        sleep(3)
        if self.__browser.current_url == origURL:
            raise Exception("Failed to enter meet code!")

    def getFromURL(self, url):
        self.__browser.get(url)
        sleep(3)
        pageSource = self.__browser.page_source
        if (("That's an error" in pageSource) or ("The meeting code that you entered doesn't work" in pageSource) or ("You can't join this video call" in pageSource)):
            raise Exception("Failed to load meet page!")

    def joinMeet(self):
        self.__browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[4]/div[1]/div/div/div').click()
        sleep(1)
        self.__browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div[4]/div[2]/div/div').click()
        sleep(1)
        self.__browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[3]/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]').click()
        sleep(3)
        self.__browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[3]/div[3]/div[6]/div[3]/div/div[2]/div[3]').click()
        sleep(3)

    def sendMessage(self, message):
        self.__browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[3]/div[3]/div[3]/div/div[2]/div/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea').send_keys(message)
        sleep(0.5)
        self.__browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[3]/div[3]/div[3]/div/div[2]/div/div[2]/span[2]/div/div[3]/div[2]').click()
        sleep(2)

    def quit(self):
        self.__browser.quit()
        return True