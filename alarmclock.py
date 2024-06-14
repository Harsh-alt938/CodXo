from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
import time
import threading
import pygame
import os

pygame.mixer.init()


alarm_running = False

def alarm(set_alarm_timer):
    global alarm_running
    while alarm_running:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            if os.path.exists("sound.wav"):
                pygame.mixer.music.load("sound.wav")
                pygame.mixer.music.play(-1) 
            else:
                messagebox.showerror("Error", "Sound file not found!")
            break

def actual_time():
    global alarm_running
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    try:
        target_time = datetime.datetime.strptime(set_alarm_timer, "%H:%M:%S")
        if target_time.time() < datetime.datetime.now().time():
            messagebox.showerror("Error", "Set time is in the past!")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid time format! Please enter valid time.")
        return
    alarm_running = True
    threading.Thread(target=alarm, args=(set_alarm_timer,)).start()
    threading.Thread(target=countdown, args=(set_alarm_timer,)).start()

def stop_alarm():
    global alarm_running
    alarm_running = False
    pygame.mixer.music.stop()

def show_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")
    messagebox.showinfo("Current Time and Date", f"Current Time: {current_time}\nCurrent Date: {current_date}")

def countdown(set_alarm_timer):
    target_time = datetime.datetime.strptime(set_alarm_timer, "%H:%M:%S")
    while alarm_running:
        now = datetime.datetime.now()
        remaining_time = target_time - now.replace(year=target_time.year, month=target_time.month, day=target_time.day)
        if remaining_time.total_seconds() > 0:
            countdown_label.config(text=f"Time left: {str(remaining_time).split('.')[0]}")
        else:
            countdown_label.config(text="Time left: 00:00:00")
            break
        time.sleep(1)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("500x500")
clock.config(bg="#f0f8ff") 


image = Image.open("clock_image.png")  
image = image.resize((100, 100), Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(image)
image_label = Label(clock, image=image, bg="#f0f8ff")
image_label.pack(pady=10)


title_label = Label(clock, text="Alarm Clock", font=("Times New Roman", 20, "bold"), bg="#f0f8ff", fg="navy")
title_label.pack(pady=10)


time_format = Label(clock, text="Enter time in 24-hour format!", fg="red", bg="#f0f8ff", font=("Arial", 12))
time_format.pack(pady=5)


addTime = Label(clock, text="Hour    Min    Sec", font=("Arial", 10), bg="#f0f8ff")
addTime.pack(pady=5)

setYourAlarm = Label(clock, text="When to wake you up", fg="blue", relief="solid", font=("Helvetica", 10, "bold"), bg="#f0f8ff")
setYourAlarm.pack(pady=5)


time_frame = Frame(clock, bg="#f0f8ff")
time_frame.pack(pady=5)


hour = StringVar()
min = StringVar()
sec = StringVar()


hourTime = Entry(time_frame, textvariable=hour, bg="pink", width=5, font=("Arial", 12))
hourTime.grid(row=0, column=0, padx=5)
minTime = Entry(time_frame, textvariable=min, bg="pink", width=5, font=("Arial", 12))
minTime.grid(row=0, column=1, padx=5)
secTime = Entry(time_frame, textvariable=sec, bg="pink", width=5, font=("Arial", 12))
secTime.grid(row=0, column=2, padx=5)


submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time, font=("Arial", 12))
submit.pack(pady=5)


stop_button = Button(clock, text="Stop Alarm", fg="red", width=10, command=stop_alarm, font=("Arial", 12))
stop_button.pack(pady=5)


time_button = Button(clock, text="Show Time", fg="red", width=10, command=show_current_time, font=("Arial", 12))
time_button.pack(pady=5)


countdown_label = Label(clock, text="Time left: 00:00:00", font=("Arial", 12), bg="#f0f8ff")
countdown_label.pack(pady=5)


footer_label = Label(clock, text="Made by: Harsh Bhardwaj", font=("Times New Roman", 12), bg="#f0f8ff", fg="black")
footer_label.pack(side=BOTTOM, pady=10)

clock.mainloop()
