import requests
from tkinter import font
import tkinter as tk

API_KEY = '*************************************'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather' # endpoint

HEIGHT = 700
WIDTH = 800

root = tk.Tk() # window

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH) # screen size
canvas.pack() # pack puts on the screen

bg_image = tk.PhotoImage(file='landscape.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') # hepls auto ajust the size of the screen

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Get Weather', font=('Courier', 18), command=lambda: chose_city(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1) # puts the button on the screen

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relwidth=1, relheight=1)

 # "get" retrieves data

def format_response(data):
    try:
        name = data['name']
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2)

        final_str =  'City: %s \n Weather: %s \n Temperature: %s ºC' %(name, weather, temperature)
    except:
        final_str = 'Error retrieving this info'

    return final_str

def chose_city(entry):
    request_url = f'{BASE_URL}?appid={API_KEY}&q={entry}' # after the ? is a query parameter (& for another query parameter), helps the filter resuts
    response = requests.get(request_url)
    if response.status_code == 200: # 200 means its sucessful
        data = response.json() #json its a type of data, returns a dictionary
    
    label['text'] = format_response(data)

root.mainloop()
