import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)

for i in range(0,10):
	GPIO.output(37,1)
	time.sleep(1)
	GPIO.output(37,0)
	time.sleep(1)

