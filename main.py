import requests
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Calcutta')
currdate = datetime.now(tz).strftime('%d-%m-%Y')

# api-endpoint
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date="
URL+=currdate
# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.json()

print(type(data))