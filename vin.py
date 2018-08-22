import json
import requests

#import pytz
#import datetime as datetime
from dateutil import parser

import sys

try:

    vin = str(sys.argv[1]) 
    year = str(sys.argv[2])
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles//DecodeVin/' + vin + '*BA?format=JSON&modelyear=' + year
    response = requests.get(url)
    data = response.json()
    make = data['Results'][5]['Value']
    model = data['Results'][7]['Value']
    veh_type = data['Results'][12]['Value']

    print('Make: '  + make)
    print('Model: ' + model)
    print('Type: '  + veh_type )

except Exception as e: print(e)           