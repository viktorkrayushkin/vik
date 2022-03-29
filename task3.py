import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup([21, 20, 10, 16,12,7,8,25],GPIO.OUT, initial = 0)

p = GPIO.PWM(24,50)
p.start()
input("Press return to stop: ")
p.stop()
GPIO.cleanup()