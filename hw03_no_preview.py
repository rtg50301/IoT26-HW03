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

# Start camera
camera.start()

# Screenshot file number
i = 0

# Stop camera and exit
def stop_camera():
    camera.stop()
    exit()

# Take an image and save it
def take_photo():
    global i
    i += 1
    camera.capture_file('/home/pi/Desktop/image_%s.jpg' % i)
    print('A photo has been taken.')
    sleep(10)

# Attach events
button.when_pressed = stop_camera
pir.when_motion = take_photo

# Wait until interrupt occurs
pause()