import requests
import json

# Airtable credentials
AIRTABLE_PAT = "patg2Q1bDyj2HcVw4.c2493796b2b197fc84ee27cbc5a2bc10c2c9f11b74528666aae6d20b247d8f38"
BASE_ID = "appvopHhf0IJnpovA"
TABLE_NAME = "Table 2"

# API endpoint
url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {AIRTABLE_PAT}"
}

# GET request
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for record in data["records"]:
        print(json.dumps(record["fields"], indent=2))
else:
    print("Error:", response.status_code, response.text)