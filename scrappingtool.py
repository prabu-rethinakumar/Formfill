from selenium import webdriver
from time import sleep
from selenium.webdriver.common import keys,action_chains
from selenium.webdriver.chrome.webdriver import Options
import sys
import selenium.common.exceptions

url = "https://www.glassdoor.com/index.htm"

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


def get_job_details(website, job_name):
    browser = web_browser()
    browser.get(website)
    sleep(2)
    form_job_data = browser.find_element_by_id("KeywordSearch")
    form_job_data.send_keys(job_name)
    form_job_location = browser.find_element_by_id("LocationSearch")
    form_job_location.clear()
    form_submit = browser.find_element_by_id("HeroSearchButton")
    form_submit.click()
    sleep(30)

get_job_details(url, "Cloud Developer")
