import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print(page.text)

# Parses the document we retrieved
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

## Children returns a list generator 
# Selects the html tag and its children
html = list(soup.children)[2]
# print(list(html.children))

body = list(html.children)[3]

p = list(body.children)[1]
# print(p.get_text())

# Finding all instances of a tag at once
allInstancesArray = soup.find_all('p')

# Finding the first instance
firstInstance = soup.find('p')

## Searching for tags by class and id
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')

# Searches for p tag with with class: outer-text
allInstancesArray = soup.find_all('p', class_= 'outer-text')

## Using CSS Selectors
# Finds all p tags inside of a div
soup.select("div p")


## Downloading Weather Data

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
# print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
# print(period)
# print(short_desc)
# print(temp)

## Extracting all the information from the page

# Select all items with class period-name inside a tombstone-container class in seven_day
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
# print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
# print(short_descs)
# print(temps)
# print(descs)

weather = pd.DataFrame({
"period": periods,
"short_desc": short_descs,
"temp": temps,
"desc":descs
})

print(weather)