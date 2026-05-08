from gpiozero import Button, MotionSensor
from time import sleep
from signal import pause
from picamera2 import Picamera2

button = Button(2)
pir = MotionSensor(4)

camera = Picamera2()

# No preview since SSH does not support GUI.
config = camera.create_still_configuration()
camera.configure(config)

camera.start()

i = 0

def stop_camera():
    camera.stop()
    exit()

def take_photo():
    global i
    i += 1
    camera.capture_file('/home/pi/Desktop/image_%s.jpg' % i)
    print('A photo has been taken.')
    sleep(10)

button.when_pressed = stop_camera
pir.when_motion = take_photo

pause()