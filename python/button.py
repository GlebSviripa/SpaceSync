
import requests
import socket
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)

buttonPin = 16

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

id = "82"
lastState = False
url = "https://webpad.com.ua/setStatus"
ip = "first"

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
fqdn = socket.getfqdn()
#print(IPAddr)
#print(fqdn)

on = 'echo 1 | sudo tee /sys/class/leds/led1/brightness'
off = 'echo 0 | sudo tee /sys/class/leds/led1/brightness'

while True:
    buttonState = GPIO.input(buttonPin)
    if buttonState != lastState:
        print(buttonState)
        if buttonState == True:
            print("false")
            r = requests.post(url, data={'id': id, 'status': "false"})
            print(r.status_code, r.reason)
            os.system(off)
        else:
            print("true")
            r = requests.post(url, data={'id': id, 'status': "true"})
            print(r.status_code, r.reason)
            os.system(on)
        lastState = buttonState


