import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("ALPR_KEY")
token = "Token {}".format(key)
regions = ['in'] # Change to your country
with open('images/truck.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': token})
pprint(response.json())
