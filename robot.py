import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.IN) #Left IR 
GPIO.setup(3,GPIO.IN) #Right IR 

GPIO.setup(4,GPIO.OUT) # Motor 1 
GPIO.setup(14,GPIO.OUT) # Motor 1 

GPIO.setup(17,GPIO.OUT) #Motor 2
GPIO.setup(18,GPIO.OUT) # Motor 2 

GPIO.setup(20,GPIO.OUT)#Trigger
GPIO.setup(21,GPIO.IN)#Echo
GPIO.setup(16,GPIO.OUT)#Servo Motor

"Move Forward"
if(GPIO.input(2)==True and GPIO.input(3)==True): 
    GPIO.output(4,True) 
    GPIO.output(14,False) 
    GPIO.output(17,True) 
    GPIO.output(18,False) 
    
"Move Left"
elif(GPIO.input(2)==False and GPIO.input(3)==True): 
    GPIO.output(4,True) 
    GPIO.output(14,True) 
    GPIO.output(17,True) 
    GPIO.output(18,False) 
    
"Move Right"
elif(GPIO.input(2)==True and GPIO.input(3)==False): 
        GPIO.output(4,True) 
        GPIO.output(14,False) 
        GPIO.output(17,True) 
        GPIO.output(18,True) 
        
"Stop"
else:
    GPIO.output(4,True) 
    GPIO.output(14,True) 
    GPIO.output(17,True) 
    GPIO.output(18,True) 
        
"Obstacle Distance"

GPIO.output(PIN_TRIGGER, False)
time.sleep(2)

print( "Calculating distance")

GPIO.output(PIN_TRIGGER, True)
time.sleep(0.00001)
GPIO.output(PIN_TRIGGER, False)

while GPIO.input(PIN_ECHO)==0:
    pulse_start_time = time.time()
    
while GPIO.input(PIN_ECHO)==1:
    pulse_end_time = time.time()
    
pulse_duration = pulse_end_time - pulse_start_time
distance = round(pulse_duration * 17150, 2)
print ("Distance:",distance,"cm")

"Servo Motor Test"
if distance is <50:
    GPIO.output(16,True)
    
"Lid Open"
