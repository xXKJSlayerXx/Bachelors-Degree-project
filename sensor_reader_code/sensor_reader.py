
from tkinter import *
import serial
from threading import Thread


port = "COM3"
dane = serial.Serial(port, 115200, timeout=1)
root = Tk()
root.geometry("600x220")
root.title('Praca Dyplomowa')
LPSLabel = Label(root, text='SENSOR READER',font=("Arial", 25))
LPSLabel.grid(row=0, column=1)
LPSLabel = Label(root, text='LPS25HB',font=("Arial", 22))
LPSLabel.grid(row=1, column=0)
HCLabel = Label(root, text='HC04-SC',font=("Arial", 22))
HCLabel.grid(row=1, column=8)
TLabel = Label(root, text='',font=("Arial", 18))
TLabel.grid(row=2, column=0)
pLabel = Label(root, text='',font=("Arial", 18))
pLabel.grid(row=3, column=0)
lLabel = Label(root, text='',font=("Arial", 18))
lLabel.grid(row=2, column=8)
def read_data():
    while True:
        data = dane.readline(12)
        data_sensor = data.decode('utf8')
        if(data_sensor.startswith('T') == True):
            temp = data_sensor.lstrip('T')
            print(temp)
            TLabel.config(text='T = ' + temp)
            root.update_idletasks()
        if(data_sensor.startswith('p') == True):
            press = data_sensor.lstrip('p')
            pLabel.config(text= 'p = ' + press)
            root.update_idletasks()
            print(press)
        if(data_sensor.startswith('l') == True):
            length = data_sensor.lstrip('l')
            print(length)
            lLabel.config(text='l = ' + length)
            root.update_idletasks()
            print(press) 

# create new thread
t1 = Thread(target=read_data)

# start the threads
t1.start()

root.mainloop()






