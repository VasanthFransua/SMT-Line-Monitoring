from Adafruit_IO import*
import RPi.GPIO as GPIO
import time

ADAFRUIT_IO_USERNAME = 'adanew_3'
ADAFRUIT_IO_KEY = 'aio_yFYS97sSoCFjz0I3ycUkX2YyKPoG'
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
try:
    counttest = aio.feeds('counttest')
except RequestError:
    counttest = Feed(name='counttest')
    counttest = aio.create_feed(counttest_feed)

#Red
red_start_lst = []
red_end_lst = []
red_total_lst = []
red_no=1
red_count=0

#Blue
blue_start_lst = []
blue_end_lst = []
blue_total_lst = []
blue_no=1
blue_count=0

#Green
green_start_lst = []
green_end_lst = []
green_total_lst = []
green_no=1
green_count=0

#Colour Sensor Config
Sensor2_s2 = 27
Sensor2_s3 = 22
Sensor2_sig2 = 17
Sensor1_s2 = 23
Sensor1_s3 = 24
Sensor1_sig1 = 25
NUM_CYCLES = 10

#Color Sensor Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Sensor1_sig1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Sensor2_sig2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Sensor1_s2,GPIO.OUT)
GPIO.setup(Sensor1_s3,GPIO.OUT)
GPIO.setup(Sensor2_s2,GPIO.OUT)
GPIO.setup(Sensor2_s3,GPIO.OUT)
  

try:
    
    while True:
        
        #Sensor 1
        #Red
        GPIO.output(Sensor1_s2,GPIO.LOW)
        GPIO.output(Sensor1_s3,GPIO.LOW)
        time.sleep(0.2)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(Sensor1_sig1, GPIO.FALLING)
        duration = time.time() - start 
        red  = NUM_CYCLES // duration
        
        #Blue
        GPIO.output(Sensor1_s2,GPIO.LOW)
        GPIO.output(Sensor1_s3,GPIO.HIGH)
        time.sleep(0.2)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(Sensor1_sig1, GPIO.FALLING)
        duration = time.time() - start
        blue = NUM_CYCLES // duration
    
        #Green
        """GPIO.output(Sensor1_s2,GPIO.HIGH)
        GPIO.output(Sensor1_s3,GPIO.HIGH)
        time.sleep(0.2)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(Sensor1_sig1, GPIO.FALLING)
        duration = time.time() - start
        green = NUM_CYCLES // duration"""
    
  
        #SENSOR 2
  
        #Red
        GPIO.output(Sensor2_s2,GPIO.LOW)
        GPIO.output(Sensor2_s3,GPIO.LOW)
        time.sleep(0.2)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(Sensor2_sig2, GPIO.FALLING)
        duration = time.time() - start 
        red2  = NUM_CYCLES // duration
        
        #Blue
        GPIO.output(Sensor2_s2,GPIO.LOW)
        GPIO.output(Sensor2_s3,GPIO.HIGH)
        time.sleep(0.2)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(Sensor2_sig2, GPIO.FALLING)
        duration = time.time() - start
        blue2 = NUM_CYCLES // duration
        
        #Green
        """GPIO.output(Sensor2_s2,GPIO.HIGH)
        GPIO.output(Sensor2_s3,GPIO.HIGH)
        time.sleep(0.2)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(Sensor2_sig2, GPIO.FALLING)
        duration = time.time() - start
        green2 = NUM_CYCLES // duration"""
    
        if red > 29000 :
            print("Sensor1: Red Starts")
            time.sleep(0.5)
            starttime=time.perf_counter()
            red_start_lst.append(starttime)
        elif red2>29000:
            time.sleep(0.5)
            endtime=time.perf_counter()
            print("Sensor1: Red {} Ends".format(red_no))
            red_end_lst.append(endtime)
            red_total_lst.append(red_end_lst[red_count]-red_start_lst[red_count])
            print("Time: {}".format(red_total_lst[red_count]))
            if red_total_lst[red_count]>15:
                aio.send('counttest',"Red {}".format(red_no))
            red_count+=1
            red_no+=1
        elif blue > 24000 :
            print("Sensor1: Blue Starts")
            time.sleep(0.5)
            starttime=time.perf_counter()
            blue_start_lst.append(starttime)
        elif blue2>24000:
            time.sleep(0.5)
            endtime=time.perf_counter()
            print("Sensor1: Blue {} Ends".format(blue_no))
            blue_end_lst.append(endtime)
            blue_total_lst.append(blue_end_lst[blue_count]-blue_start_lst[blue_count])
            print("Time: {}".format(blue_total_lst[blue_count]))
            if blue_total_lst[blue_count]>15:
                aio.send('counttest',"Blue {}".format(blue_no))
            blue_no+=1
            blue_count+=1
        

except KeyboardInterrupt:
    GPIO.cleanup()
