# import requests

# response = requests.get("https://usage.bmapsbd.com/bkoi/get/usage/details?date_from=2024-08-07&date_to=2024-08-07")
# data = response.json()
# print(data)


import requests
import csv
from datetime import datetime, timedelta

def get_last_45_days():
    today = datetime.today()
    return [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(45)]

def fetch_api_usage(date_from, date_to):
    url = f"https://usage.bmapsbd.com/bkoi/get/usage/details?date_from={date_from}&date_to={date_to}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        for record in data:
            if record["Name"] == "Sheba Platform Ltd":
                return record["Api_count"]
    return 0  

def get_usage_and_save_csv():
    dates = get_last_45_days()
    
    with open('sheba_usage_res.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["date", "count"])
        
        for date in dates:
            count = fetch_api_usage(date, date) 
            writer.writerow([date, count])

    print("CSV file saved successfully!")

get_usage_and_save_csv()
