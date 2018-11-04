# This code scrapes neighorhoods and zip codes from an online site
# We'll use these to create "neighborhood" bins for the sake of comparison


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1: url = 'https://www.health.ny.gov/statistics/cancer/registry/appendix/neighborhoods.htm'

soup = BeautifulSoup(urllib.request.urlopen(url, context=ctx).read(), 'html.parser')

tags = soup('td')

#Pass tags to this function. It will pull out each neighborhood and each set of zip codes,
#and then zip those together into a dictionary with neighborhoods paired to their zipcodes

def create_hood_dict(tag_list):
    neighborhood = []
    zip_codes = []
    for tag in tag_list:
        if str(tag).startswith('<td headers="header2">'):
            hood = tag.text.lstrip()
            neighborhood.append(hood)
        elif str(tag).startswith('<td headers="header3">'):
            zips_1 = tag.text.split(",")
            zips_2 = [zip.lstrip() for zip in zips_1]
            zip_codes.append(zips_2)
        else:
            continue
    result = zip(neighborhood, zip_codes)
    neighborhoods_local = dict(result)
    return neighborhoods_local


def persist(dict_name):
    better_dict = {}

    for k, v in dict_name.items():
        for zipcode in v:
            better_dict[zipcode] = better_dict.get(zipcode, k)

    data = test3 = pd.DataFrame.from_dict(better_dict, orient = 'index', columns = ['Neighborhood'])
    data.to_csv('calls/neighborhood.csv', mode = 'w+')
    return data
