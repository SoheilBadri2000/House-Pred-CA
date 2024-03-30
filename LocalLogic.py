import requests
import json


lng = -79.378075
lat = 43.644229
url_demographics =  'https://api.locallogic.co/v3/demographics?lng=-79.378075&lat=43.644229&lang=en'
# url_location_scores = 'https://api.locallogic.co/v3/scores?lng=-79.378075&lat=43.644229&include=quiet%2Cpedestrian_friendly%2Cgroceries%2Ccar_friendly%2Ccafes&limit=5&locale=en&geography_levels=30'
url_location_scores = f'https://api.locallogic.co/v3/scores?lng={lng}&lat={lat}'


# querystring = {"lng":"-79.378075","lat":"43.644229","lang":"en"}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept": "application/json",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
    # "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://locallogic.co/",
    "Authorization": "V3 Ei9J0EgWQDjhJ1Kp1jcmDo7Gn5H6lGZD.e6c5852b-20af-47dd-a198-0792b3d901b0",
    "Origin": "https://locallogic.co",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}

response = requests.request("GET", url_location_scores, headers=headers,)
res_json = response.json()

print(json.dumps(res_json, indent=4))

with open("locals.json", "w") as f:
    json.dump(res_json, f, indent=4)