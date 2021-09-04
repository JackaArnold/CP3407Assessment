import requests

for i in range(city):
    city = city[i]
    url1 = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b0f9a1819a779c08a683e7962e7c92b7'.format(city)

    res1 = requests.get(url1)
    data1 = res1.json()
    print(data1)

    url2 = 'http://api.weatherapi.com/v1/current.json?key=cfd762f4e3cb45d085322318210409 &q={}&aqi=no'.format(city)

    res2 = requests.get(url2)
    data2 = res2.json()
    print(data2)