import requests
from datetime import datetime
import pytz
import copy
import os
from dotenv import load_dotenv

load_dotenv()


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

res = ""
for center in data["centers"]:
    center_copy = copy.deepcopy(center)
    center_copy.pop("sessions")
    center_copy["sessions"] = []
    for session in center["sessions"]:
        if (session["min_age_limit"] == 18) and (session["available_capacity"] != 0):
            session_copy = copy.deepcopy(session)
            session_copy.pop("slots")
            session_copy.pop("session_id")
            center_copy["sessions"].append(session_copy)
    if len(center_copy["sessions"]) != 0:
        res += str(center_copy)
        res += "\n\n"

url = os.getenv("DISCORD_HOOK")

if len(res) != 0:
    res = res.replace("'", "")
    res = res.replace('"', "")
    content = "**Vaccine Stock Detected! -> *" + timestamp + "***\n" + str(res)

    split_strings = []
    n = 2000
    for index in range(0, len(content), n):
        split_strings.append(content[index : index + n])

    for i in split_strings:
        obj = {"content": i}
        requests.post(url, data=obj)