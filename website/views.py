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
info_today_sydney = df.iloc[len(df) - 8]
info_yesterday_sydney = df.iloc[len(df) - 18]
info_two_days_sydney = df.iloc[len(df) - 28]
info_today_melbourne = df.iloc[len(df) - 7]
info_yesterday_melbourne = df.iloc[len(df) - 17]
info_two_days_melbourne = df.iloc[len(df) - 27]
info_today_brisbane = df.iloc[len(df) - 6]
info_yesterday_brisbane = df.iloc[len(df) - 16]
info_two_days_brisbane = df.iloc[len(df) - 26]
info_today_losAngeles = df.iloc[len(df) - 5]
info_yesterday_losAngeles = df.iloc[len(df) - 15]
info_two_days_losAngeles = df.iloc[len(df) - 25]
info_today_chicago = df.iloc[len(df) - 4]
info_yesterday_chicago = df.iloc[len(df) - 14]
info_two_days_chicago = df.iloc[len(df) - 24]
info_today_dallas = df.iloc[len(df) - 3]
info_yesterday_dallas = df.iloc[len(df) - 13]
info_two_days_dallas = df.iloc[len(df) - 23]
info_today_longBeach = df.iloc[len(df) - 2]
info_yesterday_longBeach = df.iloc[len(df) - 12]
info_two_days_longBeach = df.iloc[len(df) - 22]
info_today_houston = df.iloc[len(df) - 1]
info_yesterday_houston = df.iloc[len(df) - 11]
info_two_days_houston = df.iloc[len(df) - 21]


@views.route('/')
def home():
    return render_template("index.html", info_today=info_today, info_yesterday=info_yesterday,
                           info_two_days=info_two_days)


@views.route('/london')
def home2():
    return render_template("london.html", info_today=info_today_london, info_yesterday=info_yesterday_london,
                           info_two_days=info_two_days_london)


@views.route('/sydney')
def home3():
    return render_template("sydney.html", info_today=info_today_sydney, info_yesterday=info_yesterday_sydney,
                           info_two_days=info_two_days_sydney)


@views.route('/melbourne')
def home4():
    return render_template("melbourne.html", info_today=info_today_melbourne, info_yesterday=info_yesterday_melbourne,
                           info_two_days=info_two_days_melbourne)


@views.route('/brisbane')
def home5():
    return render_template("brisbane.html", info_today=info_today_brisbane, info_yesterday=info_yesterday_brisbane,
                           info_two_days=info_two_days_brisbane)


@views.route('/losAngeles')
def home6():
    return render_template("losAngeles.html", info_today=info_today_losAngeles, info_yesterday=info_yesterday_losAngeles,
                           info_two_days=info_two_days_losAngeles)


@views.route('/chicago')
def home7():
    return render_template("chicago.html", info_today=info_today_chicago, info_yesterday=info_yesterday_chicago,
                           info_two_days=info_two_days_chicago)


@views.route('/dallas')
def home8():
    return render_template("dallas.html", info_today=info_today_dallas, info_yesterday=info_yesterday_dallas,
                           info_two_days=info_two_days_dallas)


@views.route('/longBeach')
def home9():
    return render_template("longBeach.html", info_today=info_today_longBeach, info_yesterday=info_yesterday_longBeach,
                           info_two_days=info_two_days_longBeach)


@views.route('/houston')
def home10():
    return render_template("houston.html", info_today=info_today_houston, info_yesterday=info_yesterday_houston,
                           info_two_days=info_two_days_houston)
