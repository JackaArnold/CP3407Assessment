import requests
import pandas as pd
from csv import writer

from website import create_app

df = pd.read_csv('cities.csv')


def averageFinder(x, y):
    avg = (x + y) / 2
    return avg


db_read = pd.read_csv("storedWeatherData.csv")


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


for i in range(len('cities.csv')):
    url1 = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b0f9a1819a779c08a683e7962e7c92b7'.format(
        df.Cities[i])
    res1 = requests.get(url1)
    data1 = res1.json()
    temp1 = data1['main']['temp'] - 273.15
    url2 = 'http://api.weatherapi.com/v1/current.json?key=cfd762f4e3cb45d085322318210409 &q={}&aqi=no'.format(
        df.Cities[i])
    res2 = requests.get(url2)
    data2 = res2.json()
    temp2 = (data2['current']['temp_c'])
    avgTemp = averageFinder(temp1, temp2)
    avgHumidity = averageFinder(data1['main']['humidity'], data2['current']['humidity'])
    avgWindSpeed = averageFinder(data1['wind']['speed'], data2['current']['wind_mph'])
    windDir = data2['current']['wind_dir']
    date = data2['current']['last_updated']
    date = date[:10]
    currentConditionIcon = data2['current']['condition']['icon']
    # Write to DB

    new_row = [date, df.Cities[i], int(avgTemp), avgHumidity, avgWindSpeed, windDir, currentConditionIcon]
    len_db_read = len(db_read) - (10 - i)
    date_tester = db_read.iloc[len_db_read][0]

    if date_tester != date:
        append_list_as_row('storedWeatherData.csv', new_row)

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
