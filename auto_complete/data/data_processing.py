import requests
import json

url = "https://geo.bmapsbd.com/bk/v2/autocomplete?text=air%20university&country=Pakistan"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open('output.jsonl', 'w') as outfile:
        for place in data.get('places', []):
            output_data = {
                "address": place['address'],
                "name": place['name']
            }
            outfile.write(json.dumps(output_data) + '\n')
    print("Data has been written to output.jsonl")
else:
    print(f"Failed to fetch data.")
