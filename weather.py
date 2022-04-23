from tkinter import *
import requests
from translate import Translator
import datetime

root = Tk()
root.title('وضعیت آب و هوا')
root.minsize(300, 450)


API = '856fd64441641af822b116556cd7cc03'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

city_name = StringVar()


def widget():
    label = Label(root, text='وضعیت آب و هوا', width=12, height=1)
    label.config(font=('sahel', 25, 'bold'), fg='Aqua', bg='Teal')
    label.grid(row=0, columnspan=2)

    label_name = Label(root, text=':نام شهر را وارد نمایید')
    label_name.config(font=('sahel', 10, 'bold'), fg='DarkSlateGray')
    label_name.grid(row=1, column=1, pady=20)

    entry_name = Entry(root, textvariable=city_name)
    entry_name.grid(row=1, column=0, pady=20)

    button_search = Button(root, text='جستجو', width=20, command=search)
    button_search.config(font=('sahel', 10, 'bold'), fg='Aqua', bg='Teal')
    button_search.grid(row=2, columnspan=2)

    label_city_name = Label(root, text=':نام شهر')
    label_city_name.config(font=('sahel', 12, 'bold'), fg='DarkSlateGray')
    label_city_name.grid(row=3, column=1, pady=10)

    label_status = Label(root, text=':وضعیت')
    label_status.config(font=('sahel', 12, 'bold'), fg='DarkSlateGray')
    label_status.grid(row=4, column=1, pady=10)

    label_temp = Label(root, text=':دما')
    label_temp.config(font=('sahel', 12, 'bold'), fg='DarkSlateGray')
    label_temp.grid(row=5, column=1, pady=10)

    label_speed_wind = Label(root, text=':سرعت باد')
    label_speed_wind.config(font=('sahel', 12, 'bold'), fg='DarkSlateGray')
    label_speed_wind.grid(row=6, column=1, pady=10)

    label_sunset = Label(root, text=':غروب خورشید')
    label_sunset.config(font=('sahel', 12, 'bold'), fg='DarkSlateGray')
    label_sunset.grid(row=7, column=1, pady=10)


def search():
    city = city_name.get()
    response = requests.get(url.format(city, API))
    response = response.json()
    translator = Translator(to_lang='Persian')

    city_trans = translator.translate(response['name'])

    label_city_name = Label(root, text=city_trans)
    label_city_name.config(font=('sahel', 10, 'bold'), fg='SteelBlue')
    label_city_name.grid(row=3, column=0, pady=10)

    status_trans = translator.translate(response['weather'][0]['main'])

    label_status = Label(root, text=status_trans)
    label_status.config(font=('sahel', 10, 'bold'), fg='SteelBlue')
    label_status.grid(row=4, column=0, pady=10)

    temp = response['main']['temp']

    label_temp = Label(root, text=(temp - 273))
    label_temp.config(font=('sahel', 10, 'bold'), fg='SteelBlue')
    label_temp.grid(row=5, column=0, pady=10)

    speed_wind = response['wind']['speed']

    label_speed_wind = Label(root, text=speed_wind)
    label_speed_wind.config(font=('sahel', 10, 'bold'), fg='SteelBlue')
    label_speed_wind.grid(row=6, column=0, pady=10)

    sunset = response['sys']['sunset']

    label_sunset = Label(root, text=datetime.datetime.fromtimestamp(sunset))
    label_sunset.config(font=('sahel', 10, 'bold'), fg='SteelBlue')
    label_sunset.grid(row=7, column=0, pady=10)

widget()


root.mainloop()