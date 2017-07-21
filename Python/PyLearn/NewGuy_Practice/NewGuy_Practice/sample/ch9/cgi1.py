#!/usr/bin/python
import sys, getopt
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

if __name__ == "__main__":
  main(sys.argv[1:])


