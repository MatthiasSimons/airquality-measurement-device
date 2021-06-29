import time
from machine import Pin, I2C, RTC, ADC
import BME280
import json
from MQ135 import MQ135
import process_data

def measureBME280():
    # function for reading the BME280 temperature, humidity and airpressure sensore
    # init sensor and library
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)
    bme = BME280.BME280(i2c=i2c)

    # replace unit strings
    temperature = float(bme.temperature.replace("C", ""))
    humidity = float(bme.humidity.replace("%", ""))
    pressure = float(bme.pressure.replace("hPa", ""))
    return temperature, humidity, pressure

def convert_to_iso(datetime): # https://github.com/ceedee666/iot_introduction/blob/master/src/project_template/main.py
    # convert
    y, m, d, _, h, mi, s, _ =  datetime
    return "{}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(y,m,d,h,mi,s)

def datetime():
    return convert_to_iso(RTC().datetime())

def measure():
    # function for getting timestamp and sensor values; creating message map
    # set variables to None so message can be send if timestamp/sensor cant get read
    timestamp, temperature, humidity, pressure, ppm, prognosis = None, None, None, None, None, None

    # get timestamp
    try:
        timestamp = datetime()
    except Exception as e:
        print('Cannot read Datetime: ' + str(e))

    # read BME280 sensor
    try:
        temperature, humidity, pressure = measureBME280()
    except Exception as e:
        print('Cannot read BME280: ' + str(e))

    # read MQ135 sensor
    try:
        mq135 = MQ135(0)
        mq135_measure = mq135.measure(temperature, humidity)
        ppm = mq135_measure["corrected_ppm"]
    except Exception as e:
        print('Cannot read MQ135: ' + str(e))

    try:
        # get prognosed value, value is not used yet because of low quality data
        prognosis = process_data.prognosis(ppm)
    except Exception as e:
        print('Cannot calculate prognosis: ' + str(e))

    # message = {
    #     'timestamp': timestamp,
    #     'temperature': temperature,
    #     'ppm': ppm,
    #     'prognosis': prognosis,
    # }

    message = {
        'timestamp': timestamp,
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'ppm': ppm,
    }
    return message
