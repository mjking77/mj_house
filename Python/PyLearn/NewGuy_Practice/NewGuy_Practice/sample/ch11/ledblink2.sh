#!/bin/bash
       cd /sys/class/gpio
       echo “Opening port” $1
       echo $1 > export
       echo “And making it an output”
       echo out > gpio$1/direction
       for I in {1..5}
       do
           echo “Setting value to 1”
           echo 1 > gpio$1/value
           sleep 1
           echo “Setting value to 0”
           echo 0 > gpio$1/value
           sleep 1
done
       echo “Closing port” $1
       echo $! > unexport
       cd /home/pi
