from firebase import firebase
firebase = firebase.FirebaseApplication('Add your firebase database link')
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(24, GPIO.IN)    # set GPIO24 as input x (button)
GPIO.setup(25, GPIO.IN)    # set GPIO25 as input y (button)
GPIO.setup(23, GPIO.OUT)   # set GPIO23 as out
print(time.localtime())  
try:  
    while True:

        # this will carry on until you hit CTRL+C
        r = firebase.get('/message',None)
        u = firebase.get('/Time/Hours',None)                                    ##All From Firebase
        v = firebase.get('/Time/Minutes',None)
        #t = firebase.put('status','Status','Status is ON')
        print(r)
        print(u)
        print(v)
        #print (t)

        if(r =='On'):
            GPIO.output(23, 1)
        elif(r =='Off'):
            GPIO.output(23, 0)
           

        hour = time.localtime().tm_hour                                         ##Real Time on Rpi
        minute = time.localtime().tm_min
        sec = time.localtime().tm_sec
##        if(hour>12 and hour!=0):
##            hr = hour-12                                                        ##PM Time
##        elif(hour == 0):
##            hr = 12
##        else:
##            hr = hour                                                           ##AM Time                  
       
        if(minute == v and hour == u):
            print("Time to water them plants")                                  ##Timer Running
            GPIO.output(23, 1)
            t = firebase.put('status','Status','Timer On')
        else:
            if GPIO.input(24):
                print("High Moisture")                                          ##High Moisture
                GPIO.output(23, 0)
                t = firebase.put('status','Status','High Moisture')
               
            elif GPIO.input(25):
                print("Low Moisture")                                           ##Low Moisture
                GPIO.output(23, 1)
                t = firebase.put('status','Status','Low Moisture')
#print(time.localtime())
##print("hour:")
##hour = time.localtime().tm_hour
##print(hour)
##print("min")
##minute = time.localtime().tm_min
##print(minute)
##sec = time.localtime().tm_sec
##print("sec:")
##print(sec)
 
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  