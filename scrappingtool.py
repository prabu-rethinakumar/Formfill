from selenium import webdriver
from time import sleep
from selenium.webdriver.common import keys,action_chains
from selenium.webdriver.chrome.webdriver import Options
import sys
import selenium.common.exceptions


def web_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-plugins-discovery')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")  # This make Chromium reachable
    chrome_options.add_argument("--no-default-browser-check")  # Overrides default choices
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-default-apps")

    driver = "C:\\Users\pprra\Downloads\chromedriver\\chromedriver.exe"
    browser1 = webdriver.Chrome(driver, chrome_options=chrome_options)

    return browser1


website = "https://www.glassdoor.com/index.htm"
browser = web_browser()
browser.get(website)

