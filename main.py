import requests
from datetime import datetime
import pytz
import copy

tz = pytz.timezone("Asia/Calcutta")
currdate = datetime.now(tz).strftime("%d-%m-%Y")
timestamp = datetime.now(tz).strftime("%Y:%m:%d %H:%M:%S %Z %z")

# api-endpoint
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date="
URL += currdate
# sending get request and saving the response as response object
r = requests.get(url=URL)

# extracting data in json format
data = r.json()

res = []
for center in data["centers"]:
    center_copy = copy.deepcopy(center)
    center_copy.pop("sessions")
    center_copy["sessions"] = []
    for session in center["sessions"]:
        if (session["min_age_limit"] == 18) and (session["available_capacity"] != 0):
            center_copy["sessions"].append(session)
    if len(center_copy["sessions"]) != 0:
        res.append(center_copy)

print(len(res))
