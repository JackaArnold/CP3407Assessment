import pandas as pd
df = pd.read_csv('storedWeatherData.csv')
print(df.iloc[0][1])


string = '2021-10-30 21:30'
string1 = string[:10]
print(string1)