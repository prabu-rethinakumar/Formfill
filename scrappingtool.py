from selenium import webdriver
from time import sleep
# from selenium.webdriver.common import keys,action_chains
# from selenium.webdriver.chrome.webdriver import Options
import sys
from selenium.common.exceptions import *
# import pprint
url = "https://www.glassdoor.com/index.htm"


# This Method is used to find the number of pages of results available
def get_total_pages(browser):
    total = browser.find_element_by_id("TotalPages").get_attribute("value")
    print("Search Results span across {} pages ".format(total))
    return total

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
    print("Initialize Browser")
    browser = web_browser()
    print("Logging into the Web browser")
    browser.get(website)
    sleep(2)
    form_job_data = browser.find_element_by_id("KeywordSearch")
    print("Start searching for Job title {}".format(job_name))
    try:
        form_job_data.send_keys(job_name)
        form_job_location = browser.find_element_by_id("LocationSearch")
        form_job_location.clear()
        form_submit = browser.find_element_by_id("HeroSearchButton")
        form_submit.click()
        print("Job Search Initialized Successfully")

    except NoSuchElementException:

        print("Failed to Click Search button")
        sys.exit("Error Message")

    sleep(2)
    iter = get_total_pages(browser)

#   save_url = browser.current_url
#   print("Save url contains :{}".format(save_url))
#   sleep(2)
#   job_list = browser.find_element_by_class_name("jl")
#   job_link_list = browser.find_elements_by_partial_link_text("/partner/jobListing.htm?")
    print("Started collecting Job listings")

    job_link_list = browser.find_elements_by_class_name("jobLink")
    sleep(2)
    j = {}
    for i in job_link_list:
        hyper_link = i.get_attribute('href')
        job_list_id = hyper_link[len(hyper_link)-10:]
        j.setdefault(job_list_id, hyper_link)
#       print("Job Listing : {} URL : {}".format(job_list_id, hyper_link))
    if len(j) > 0:
        print("Job list preparation successful")
    else:
        print("No Jobs found, please verify the search criteria")
#   pprint.pprint(j)


get_job_details(url, "Cloud Developer")
