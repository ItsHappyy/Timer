import time
import tkinter as tk
from tkinter import *

# Funkcja generowania czasu
def tick(time1 =''):
    time2 = time.strftime('%I:%M:%S')
    if time2 != time1:
        time1 = time2
        clock_frame.config(text=time2)
    clock_frame.after(200, tick)

window = tk.Tk()
window.title("Timer Application")   # Tytuł okna
clock_frame = tk.Label(window, font=('Monaco 65 bold'),bg = '#52217a', fg='#0092d5') # Zmiana Koloru Okan
clock_frame.pack(fill='both', expand=1) 
window.geometry('700x500')  # Rozmiar okna
window.configure(background="lightgreen")   

tick()  # Wywołanie funkcji 

# Koniec pętli
window.mainloop()