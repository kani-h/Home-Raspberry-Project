import Adafruit_DHT
import time
from datetime import datetime
from home_service.hygrothermograph_service import HygrothermographService

sensor = Adafruit_DHT.DHT11
pin = 4
starttime = time.time()
hygrothermograph_service = HygrothermographService()

while True:
    time.sleep(1)
    if datetime.today().second % 30 == 0:
        print(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            hygrothermograph_service.create({'region': 'LIVING_ROOM', 'temperature': temperature, 'humidity': humidity})
        else:
            print('Failed to get reading. Try again!')