import time

import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime, date


class Weather:
    def __init__(self):
        self.weather_source = 'https://ua.sinoptik.ua/погода-'

    def weather_now(self, city):
        temperature, time = self.get_weather(city)

        self.write_to_db(city, temperature, time)

    def get_weather(self, city):
        req = requests.get(self.weather_source + city)
        soup = BeautifulSoup(req.content, "html.parser")

        temp = soup.find("p", {"class": 'today-temp'})
        now = soup.find("p", {"class": 'today-time'})

        temp = temp.text.split()
        now = now.text.split()

        temp = temp[0]
        now = now[3]

        return [temp, now]

    def write_to_db(self, city, temperature, time_weather):

        con = sqlite3.connect("weather.db")
        cursor = con.cursor()

        try:
            cursor.execute("""CREATE TABLE weather
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            city TEXT,
                            temperature TEXT,
                            time TEXT,
                            pc_time TEXT
                            )
                        """)
        except sqlite3.OperationalError as e:
            print(e)

        pc_time = str(date.today()) + " " + datetime.now().strftime("%H:%M")

        cursor.execute('INSERT INTO weather (city,temperature, time, pc_time) VALUES (?,?,?,?)',
                       [city, temperature, time_weather, pc_time])
        con.commit()


weather = Weather()

city = input("Введіть місто для запису в базу даних (івано-франківськ, київ, львів і т.д.): ")
delay = int(input("Введіть затримку: "))

while True:
    try:
        print("What Weather")
        weather.weather_now(city)
        print("Complate")
    except:
        print("Error")


    time.sleep(delay*60)
