#!/bin/bash
       cd /sys/class/gpio
       echo “Opening port” 4
       echo 4 > export
       echo “And making it an output”
       echo out > gpio4/direction
       for I in {1..5}
       do
           echo “Setting value to 1”
           echo 1 > gpio4/value
           sleep 1
           echo “Setting value to 0”
           echo 0 > gpio4/value
           sleep 1
done 
       echo “Closing port” 4
       echo 4 > unexport
       cd /home/pi