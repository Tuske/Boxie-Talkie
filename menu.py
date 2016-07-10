from time import sleep
from random import randint
from datetime import datetime
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import spur
import os
import pyglet
from Sunetp import spres
from Sunett import stemp
from Sunetu import sum
from pong import pong
from rr import rr
from rrppi import rrp
sleep(10)
shell = spur.LocalShell()
shell.spawn(["python","/home/pi/bt/pp.py"])
v=["Temperatura","Presiunea","Umiditatea","Piatra,Foarfeca\n,Hartie","Inchidere"]
GPIO.setmode(GPIO.BCM)
#20
GPIO.setup(16,GPIO.IN, GPIO.PUD_UP)
GPIO.setup(20,GPIO.IN, GPIO.PUD_UP)
channel=[16,20]
lcd_rs        = 25
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
#30
lcd_columns = 17
lcd_rows    = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows)

GPIO.add_event_detect(16, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(20, GPIO.RISING, bouncetime=300)
def clock():
    while True:
        lcd.clear()
        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
        sleep(1)
        if(GPIO.event_detected(16)):
            break

def menu():        
    clock()
    lcd.clear()
    i=0
    ok=0
    while (i<5):
        if ok==0: 
            lcd.clear()
            lcd.message(v[i])
            sleep(1)
            ok=1
        if GPIO.event_detected(20):
            if i==0:
#60
                shell = spur.LocalShell()
                result = shell.run(["python","/home/pi/bt/temp.py"])
                temp=result.output
                stemp(int(temp))
                lcd.clear()
                temp="Temperatura\n este :"+str(temp)
                lcd.message(temp)
                ok=0
                while not GPIO.event_detected(16):
                    pass
            if i==1:
                shell = spur.LocalShell()
                result = shell.run(["python","/home/pi/bt/pres.py"])
                pres=result.output
                lcd.clear()
                spres(int(pres))
                pres="Presiunea\n este: " +str(pres)
                lcd.message(pres)
                ok=0
                while not GPIO.event_detected(16):
                    pass
            if i==2:
                shell = spur.LocalShell() 
                result = shell.run(["python","/home/pi/bt/hum.py"])
                um=result.output
                sum(int(um))
                lcd.clear()
                lcd.message("Umiditatea"+'\n'+"este :"+um)
                ok=0
                while not GPIO.event_detected(16):
                    pass
            if i==3:
                x=["Piatra","Foarfeca","Hartie"]
 		computer = x[randint(0,2)]
		j=0
		player = False
		ok1=0
 		while True:
                 if ok1==0: 
                     lcd.clear()
                     t = ["Alegeti piatra?\n  Nu        Da","Alegeti Foarfeca?\n  Nu        Da","Alegeti Hartie?\n  Nu        Da"]
                     lcd.message(t[j])
                     sleep(1)
                     ok1=1       
		 if GPIO.event_detected(20):
                     if j==0:
                        player = "Piatra"
                        lcd.clear()
                        lcd.message("Ati ales:\n Piatra")
                        sleep(2)
                        ok1=0
                        break
                     if j==1:
                        player = "Foarfeca"
                        lcd.clear()
                        lcd.message("Ati ales:\n Foarfeca")
                        sleep(2)
                        ok1=0
                        break
                     if j==2:
                        player = "Hartie"
                        lcd.clear()
                        lcd.message("Ati ales:\n Hartie")
                        sleep(2)
                        ok1=0
                        break   
                 else:
                     if GPIO.event_detected(16):
                        if j<2:
                            j+=1
                        else:
                            j=0
                        ok1=0
                print (player,computer)        
                if player == computer:
                    lcd.clear()
                    lcd.message("Egal")
                elif player == x[0]:
                    if computer == x[2]:
                       lcd.clear()
                       lcd.message("Ai pierdut,\nOponent:Hartie") 
                    else:
                       lcd.clear()
                       lcd.message("Ai castigat,\nOponent:Foarfeca")
                elif player == x[1]:
                    if computer == x[0]:
                       lcd.clear()
                       lcd.message("Ai pierdut,\nOponent:Piatra") 
                    else:
                       lcd.clear()
                       lcd.message("Ai castigat,\nOponent:Hartie")
                elif player == x[2]:
                    if computer == x[1]:
                       lcd.clear()
                       lcd.message("Ai pierdut,\nOponent:Foarfeca") 
                    else:
                       lcd.clear()
                       lcd.message("Ai castigat,\nOponent:Piatra")
                ok=0
                while not GPIO.event_detected(16):
                    pass
            
            if i==4:
                rr()
                lcd.clear()
                sleep(2)
                rrp()
        else:
            if GPIO.event_detected(16):
                i+=1
                ok=0
           
while True:
    menu()
