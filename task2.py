import RPi.GPIO as GPIO
import time
dac = [26,19,13,6,5,11,9,10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(decimal):
    return[int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    for i in range(256):
    #while True:
      #  inputStr = input("Enter a value between 0 and 255('q' to exit)> ") 

      #  if inputStr.isdigit():
        value = int(i)

          #  if value >= levels:
           #     print("The value is too large, try again")
            #    continue

        signal = bin2dac(value)
        time.sleep(0.009)
        #valtage = value / levels * maxVoltage
            #print("Entered value = {:^3} -> {}, output valtage = {:.2f}".format(value, signal, valtage))
        
       # elif inputStr == 'q':
        #    break
      #  else:
         #   print("Enter a positive integer")
        #    continue
    for j in range(255,-1,-1):
    #while True:
      #  inputStr = input("Enter a value between 0 and 255('q' to exit)> ") 

      #  if inputStr.isdigit():
        value = int(j)

          #  if value >= levels:
           #     print("The value is too large, try again")
            #    continue

        signal = bin2dac(value)
        time.sleep(0.009)

#except KeyboardInterrupt:
    #print("the program was stoped by the keyboard")
#else:
   # print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")