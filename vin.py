import json
import requests

from dateutil import parser

import sys

try:

    vin = str(sys.argv[1]) 
    year = str(sys.argv[2])
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles//DecodeVin/' + vin + '*BA?format=JSON&modelyear=' + year
    print(f"Url: {url}")
    response = requests.get(url)
    print(f"response:{response}")
    data = response.json()
    # print(f"data: {data}")
    make = data['Results'][5]['Value']
    model = data['Results'][7]['Value']
    veh_type = data['Results'][12]['Value']
    for result in range(len(data['Results'])):
        print(data['Results'][result])


except Exception as e: print(e)        
