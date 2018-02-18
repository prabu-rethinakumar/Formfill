from selenium import webdriver
from time import sleep
import json
# from selenium.webdriver.common import alert
# from selenium.webdriver.chrome.webdriver import Options
import sys
from selenium.common.exceptions import *
# import pprint
url = "https://www.glassdoor.com/index.htm"


# This Method is used to find the number of pages of results available
def get_total_pages(browser):
    total = browser.find_element_by_id("TotalPages").get_attribute("value")
    print("Search Results span across {} pages ".format(total))
    return int(total)


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


def get_jobs_from_page(output_list, browser):
    listings = browser.find_elements_by_class_name("jobLink")

    for i in listings:
        hyper_link = i.get_attribute('href')
        job_list_id = hyper_link[len(hyper_link)-10:]
        output_list.setdefault(job_list_id, hyper_link)
    return output_list


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
        sleep(2)
        form_submit = browser.find_element_by_id("HeroSearchButton")
        form_submit.click()
        print("Job Search Initialized Successfully")

    except NoSuchElementException:

        print("Failed to Click Search button")
        sys.exit("Error Message")

    sleep(5)
    itern = get_total_pages(browser)

    print("Started collecting Job listings")
    j = {}
    for i in range(1, itern + 1, 1):
        print("Working on Page {} ".format(i))

        try:
            browser.find_element_by_class_name("mfp-close").click()
        except NoSuchElementException:
            pass

        get_jobs_from_page(j, browser)

        try:
            browser.find_element_by_class_name("next").click()
            print("Clicked next page")
            sleep(5)

        except NoSuchElementException:
            print("Reached Last page in search..exiting")
        except WebDriverException:
            sleep(2)
            print("Some pop ups came out, don't worry I am handling it")
            try:
                browser.find_element_by_class_name("mfp-close").click()
            except NoSuchElementException:
                pass

        if i == itern + 1:
            print("Collecting data from last page")
            get_jobs_from_page(j, browser)

    sleep(2)

    if len(j) > 0:
        print("Total jobs found in all pages : {} ". format(len(j)))
        print("Job list preparation successful")
        file = open("C:\\Users\pprra\PycharmProjects\Formfill\output_files\\{}.txt".format(job_name),
                    mode="w+")
        for k, v in j.items():
            file.write(str(k) + ' : ' + str(v) + '\n')

        file.close()
    else:
        print("No Jobs found, please verify the search criteria")



get_job_details(url, "Cloud Developer")
