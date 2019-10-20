
import requests
import socket
import RPi.GPIO as GPIO

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
print(IPAddr)
print(fqdn)

while True:
    buttonState = GPIO.input(buttonPin)
    if buttonState != lastState:
        print(buttonState)
        if buttonState == False:
            print("false")
            r = requests.post(url, data={'id': id, 'status': "false"})
            print(r.status_code, r.reason)
        else:
            print("true")
            r = requests.post(url, data={'id': id, 'status': "true"})
            print(r.status_code, r.reason)
        lastState = buttonState


