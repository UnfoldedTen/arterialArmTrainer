from tkinter import *   
import wiringpi
import platform
import RPi.GPIO as GPIO

def setPwm(newvalue):
    pwmValue.set(newvalue)
    pwmled = pwmWrite(led, pwmValue / 60)

def on_closing():
    print("Clean up")
    pwmled.stop()
    GPIO.cleanup()
    print("bye")
    master.destroy()

mode = GPIO.BCM
led = 16

print("Raspberry Pi board revision: "
      + str(GPIO.RPI_INFO['P1_REVISION']))
print("Machine: "
      + platform.machine())
print("Processor: "
      + platform.processor())
print("System: "
      + platform.system())
print("Version: "
      + platform.version())
print("Uname: "
      + str(platform.uname()))
print("Python version: "
      + platform.python_version())
print("RPi.GPIO version: "
      + str(GPIO.VERSION))

GPIO.setmode(mode)
GPIO.setup(led, GPIO.OUT)
pwmled = GPIO.PWM(led, 50)
pwmled.start(0)

master = Tk()

pwmValue = StringVar()
label = Label(master, textvariable=pwmValue, relief=RAISED )
label.pack()

slider = Scale(master, from_=40, to=180, orient=HORIZONTAL, command=setPwm)
slider.pack()

master.protocol("WM_DELETE_WINDOW", on_closing)
mainloop()