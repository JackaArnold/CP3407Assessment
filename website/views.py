from flask import Blueprint, render_template
import pandas as pd

views = Blueprint('views', __name__)
df = pd.read_csv('C:/Users/Jacka/PycharmProjects/CP3407Assessment/storedWeatherData.csv')
info_today = df.iloc[len(df) - 10]
info_yesterday = df.iloc[len(df) - 20]
info_two_days = df.iloc[len(df) - 30]
info_today_london = df.iloc[len(df) - 9]
info_yesterday_london = df.iloc[len(df) - 19]
info_two_days_london = df.iloc[len(df) - 29]


@views.route('/')
def home():
    return render_template("index.html",info_today=info_today, info_yesterday=info_yesterday, info_two_days=info_two_days)


@views.route('/london')
def home1():
    return render_template("london.html",info_today=info_today_london, info_yesterday=info_yesterday_london, info_two_days=info_two_days_london)