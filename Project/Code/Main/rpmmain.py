from Adafruit_IO import*
import serial, string, time

output = " "
ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=8)
ADAFRUIT_IO_USERNAME = 'adanew_3'
ADAFRUIT_IO_KEY = 'aio_yFYS97sSoCFjz0I3ycUkX2YyKPoG'
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
try:
    rpmtest = aio.feeds('rpmtest')
except RequestError:
    rpmtest_feed = Feed(name='rpmtest')
    rpmtest_feed = aio.create_feed(rpmtest_feed)
    
try:
    
    while True:
        while output != "":
            output = ser.readline()
            print (int(output))
            aio.send('rpmtest', int(output))
        output = " "
except KeyboardInterrupt:
    pass