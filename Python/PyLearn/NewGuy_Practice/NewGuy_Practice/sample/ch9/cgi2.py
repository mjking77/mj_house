#!/usr/bin/python
# author: Powen Ko
import time, RPi.GPIO as GPIO
import sys, getopt

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
print "Content-Type: text/plain;charset=utf-8"


def main(argv):
  inputfile7=''
  inputfile11=''
  try:
     opts, args = getopt.getopt(argv,"ha:b:")
  except getopt.GetoptError:
     print 'chi1.py -a <on/off> -b <om/off>'
     sys.exit(2)
  for opt, arg in opts:
      if opt == '-h':
         print 'cgi1.py -a <on> -b <off1> '
         sys.exit()
      elif opt in ("-a"):
         inputfile7 = arg
      elif opt in ("-b" ):
         inputfile11 = arg
  print 'Input Pin7"', inputfile7
  print 'Input Pin11"',inputfile11
  if inputfile7.upper()=="ON":
     print("pin7 ON")
     GPIO.output(7,1)
￼  else:
     print("pin7 OFF")
     GPIO.output(7,0)
  if inputfile11.upper()=="ON":
     print("pin11 ON")
     GPIO.output(11,1)
  else:
     print("pin11 OFF")
     GPIO.output(11,0)


if __name__ == "__main__":
  main(sys.argv[1:])


