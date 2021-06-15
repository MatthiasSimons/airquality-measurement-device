import time
from machine import Pin, I2C, RTC, ADC
import BME280
import json
from MQ135 import MQ135

def measureBME280():
    # BME280
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)
    bme = BME280.BME280(i2c=i2c)

    temperature = float(bme.temperature.replace("C", ""))
    humidity = float(bme.humidity.replace("%", ""))
    pressure = float(bme.pressure.replace("hPa", ""))
    return temperature, humidity, pressure

def convert_to_iso(datetime):
    y, m, d, _, h, mi, s, _ =  datetime
    return "{}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(y,m,d,h,mi,s)

def datetime():
    return convert_to_iso(RTC().datetime())

def measure():
    timestamp, temperature, humidity, pressure, ppm = None, None, None, None, None

    try:
        timestamp = datetime()
    except Exception as e:
        print('Cannot read Datetime: ' + str(e))

    try:
        temperature, humidity, pressure = measureBME280()

    except Exception as e:
        print('Cannot read BME280: ' + str(e))

    mq135 = MQ135(0)
    print(mq135.get_resistance())
    mq135_measure = mq135.measure(temperature, humidity)
    ppm = mq135_measure["corrected_ppm"]

    message = {
        'timestamp': timestamp,
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'ppm': ppm,
    }
    return message









