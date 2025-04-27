import requests
from bs4 import BeautifulSoup
import csv
import os

def fetch_gdp_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for invalid responses
        return response.text
    except requests.HTTPError as e:
        print(f"❌ HTTP Error occurred: {e}")
        return None

def parse_gdp_data(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find("table", {"class": "wikitable"})
    rows = table.find_all("tr")
    
    data = []
    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) >= 2:
            country = cols[0].text.strip()
            gdp = cols[1].text.strip()
            year = cols[2].text.strip()
            data.append([country, gdp, year])
    
    return data

def save_to_csv(data, filename="gdp.csv"):
    # Ensure the './data' folder exists
    data_folder = './data'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    
    file_path = os.path.join(data_folder, filename)
    
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Country", "GDP", "Year"])  # Header
        writer.writerows(data)
    
    print(f"✅ Saved data to {file_path}")

def main():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    
    # Step 1: Fetch HTML data
    html = fetch_gdp_data(url)
    if html is None:
        return
    
    # Step 2: Parse and extract data
    gdp_data = parse_gdp_data(html)
    
    # Step 3: Save data to CSV in the './data' folder
    save_to_csv(gdp_data)

if __name__ == "__main__":
    main()
