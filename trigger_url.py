import os
import urllib3
import certifi
#import json
from bs4 import BeautifulSoup

url = 'https://www.google.com'
http_trigger = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where(),)
content = http_trigger.request(method='GET', url='https://manh.wd5.myworkdayjobs.com/en-US/External/job/Atlanta-GA/Senior-Support-Consultant_8659/apply')

print(content.data)
soup = BeautifulSoup(content.data, 'html.parser')
print(soup.input)
#forms = soup.form
print(soup.prettify())


