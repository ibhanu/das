import requests
from pprint import pprint
regions = ['in'] # Change to your country
with open('images/truck3.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token e5414f241d2c1bebca50c119aa7056d332bef0d4'})
pprint(response.json())
