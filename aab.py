import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
import json
import datetime
import time
import pygame
pygame.init()
pygame.mixer.init()
import threading
i=time.time()

# Initialize global variables
city = ""
country = ""
timezone = ""
datenow = ""
timenow = ""
fajr = ""
duhr = ""
asr = ""
maghrib = ""
isha = ""


#===============Functions======================================
def fetch_city_country():
    global city,country,timezone
    try:
        resp1=requests.get("https://api.ipify.org/?format=json")
        myip=resp1.text
        data1=json.loads(myip)
        ip_ad=data1["ip"]
    
        resp2=requests.get("https://ipinfo.io/"+ip_ad+"/geo")
        res=resp2.text
        data2=json.loads(res)
        
        #=====================================
        ip=data2["ip"]
        country=data2["country"]
        city=data2["city"]
        timezone=data2["timezone"]
        print(ip,country,city,timezone)
    except Exception as e:
        messagebox.showerror(title="Error",message=str(e))
        city="No connection !"
def prayer_timings(city, country):
    global fajr, duhr, asr, maghrib, isha
    try :
        url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=9"
        response = requests.get(url)
        info = response.json()
        timing = info["data"]["timings"]
        fajr = timing["Fajr"]
        duhr = timing["Dhuhr"]
        asr = timing["Asr"]
        maghrib = timing["Maghrib"]
        isha = timing["Isha"]
    except Exception as e :
        messagebox.showerror(title="Error",message=str(e))   
        fajr,duhr,asr,maghrib,isha="00:00","00:00","00:00","00:00","00:00"   
def date_time():
    global datenow,timenow
    try :
        datetim=datetime.datetime.now()
        datenow=datetim.date()
        hr=datetim.hour
        min=datetim.minute
        timenow=(f"{hr:02}:{min:02}")
        print (timenow) 
    except Exception as e :
        messagebox.showerror(title="Error",message=str(e))     
def adhan():
    while True :
        try :
            if timenow=="01:18" or timenow=="23:59" or timenow=="23:28" or timenow==maghrib or timenow==isha :
                print (timenow)
                print("adhan time")
                pygame.mixer.music.load("C:\\Users\\HHSS\\Desktop\\Learn_Python\\Tkinter\\adhan.mp3")
                pygame.mixer.music.play() 
                
                                
        except Exception as e :
            messagebox.showerror(title="Error",message=str(e))


# Create the Tkinter application window
root = tk.Tk()
root.title("Prayer Timing")
root.resizable(False, False)
root.geometry("800x427+250+100")
root.iconbitmap("C:\\Users\\HHSS\\Desktop\\Learn_Python\\Tkinter\\prayer.ico")



# Load and resize the background image
background_image = Image.open("fnll.jpg")
background_image = background_image.resize((800, 427), Image.BOX)
background_photo = ImageTk.PhotoImage(background_image)

# Create a Canvas widget to display the resized background image
canvas = tk.Canvas(root, width=800, height=427)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

title=tk.Label(root,text="Prayer Timing",bg="#EAEEE9",fg="#4e627a",font=("Gabriola", 24),width=23,justify="center")
title.place(x=240,y=5)

# Labels to display location and prayer timings
'''fetch_city_country()
date_time()
prayer_timings(city,country)'''

t1=threading.Thread(target=fetch_city_country)
t2=threading.Thread(target=date_time)



t1.start()
t2.start()


t1.join()
t2.join()


prayer_timings(city,country)



location_label = tk.Label(root, text=f'''{city},{country}\n\n {datenow}''' ,bg="#ae814a",fg="#fae5a4", font=("Comic Sans MS", 11),justify="left")
location_label.place(x=31, y=20)
photo=tk.PhotoImage(file="C:\\Users\\HHSS\\Desktop\\Learn_Python\\Tkinter\\location.png")
res=photo.subsample(3,3)
lbl=tk.Label(root,image=res,bg="#ae814a")
lbl.place(x=7,y=18)

photo1=tk.PhotoImage(file="C:\\Users\\HHSS\\Desktop\\Learn_Python\\Tkinter\\calendar.png")
res1=photo1.subsample(3,3)
lbl1=tk.Label(root,image=res1,bg="#ae814a")
lbl1.place(x=7,y=60)

fajr_label = tk.Label(root, text=fajr,bg="#84623c",fg="white", font=("Footlight MT Light", 20))
fajr_label.place(x=45, y=310)

duhr_label = tk.Label(root, text=duhr,bg="#a08536",fg="white", font=("Footlight MT Light", 20))
duhr_label.place(x=208, y=310)

asr_label = tk.Label(root, text=asr, bg="#4e627a",fg="white",font=("Footlight MT Light", 20))
asr_label.place(x=368, y=310)

maghrib_label = tk.Label(root, text=maghrib,bg="#7d342d",fg="white", font=("Footlight MT Light", 20))
maghrib_label.place(x=528, y=310)

isha_label = tk.Label(root, text=isha,bg="#1f1619",fg="white", font=("Footlight MT Light", 20))
isha_label.place(x=688, y=310)



f=time.time()

print(f-i)
# Main loop
root.mainloop()


##if you want place location and date in the left buttom
##'''location_label = tk.Label(root, text=f'''{city},{country}\n\n {datenow}''' ,bg="#84623c",fg="#fae5a4", font=("Comic Sans MS", 11),justify="left")
##location_label.place(x=31, y=350)
##photo=tk.PhotoImage(file="C:\\Users\\HHSS\\Desktop\\Learn_Python\\Tkinter\\location.png")
##res=photo.subsample(3,3)
##lbl=tk.Label(root,image=res,bg="#84623c")
##lbl.place(x=7,y=348)

##photo1=tk.PhotoImage(file="C:\\Users\\HHSS\\Desktop\\Learn_Python\\Tkinter\\calendar.png")
##res1=photo1.subsample(3,3)
##lbl1=tk.Label(root,image=res1,bg="#84623c")
##lbl1.place(x=7,y=390)'''