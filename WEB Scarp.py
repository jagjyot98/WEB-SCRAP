import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XoelzYgzZPY')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find_all('a')) #also find  images,short descriptions,etc
week = soup.find(id='seven-day-forecast-body')
# print(week.get_text())
# print(week.find_all('li'))

# list comprehension( contain all of tombstone container)
items = week.find_all(class_='tombstone-container')
# print(items[0].get_text())

# creating lists for various Attributes
period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
'''
print(period_names)
print(short_descriptions)
print(temperatures)
'''
# dictionary
weather_stf = pd.DataFrame(
    {
      'Period': period_names,
      'Description': short_descriptions,
      'temperatures': temperatures,
    })

print(weather_stf)
# weather_stf.to_csv('Weather.csv')

plt.plot(temperatures, period_names)
plt.show()
