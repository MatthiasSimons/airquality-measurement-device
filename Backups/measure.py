import json
import time
from machine import Pin, I2C, RTC, ADC
import BME280
from MQ135 import MQ135


# 400ppm – 750ppm: Good for health
# 750 ppm – 1200 ppm: Take care
# 1200 ppm (and above): Harmful to health

def measureBME280():
    # BME280
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)
    bme = BME280.BME280(i2c=i2c)

    temperature = float(bme.temperature.replace("C", ""))
    humidity = float(bme.humidity.replace("%", ""))
    pressure = float(bme.pressure.replace("hPa", ""))
    return temperature, humidity, pressure


def measureMQ135(temperature=20., humidity=25.):
    # MQ135
    mq135 = MQ135(0)  # analog PIN 0

    temperature, humidity = float(temperature), float(humidity)
    rzero = mq135.get_rzero()
    corrected_rzero = mq135.get_corrected_rzero(temperature, humidity)
    resistance = mq135.get_resistance()
    ppm = mq135.get_ppm()
    corrected_ppm = mq135.get_corrected_ppm(temperature, humidity)

    return corrected_ppm

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

    try:
        ppm = measureMQ135(temperature, humidity)

    except Exception as e:
        print('Cannot read MQ135: ' + str(e))

    message = {"datetime": timestamp, "temperature": temperature, "humidity": humidity, "pressure": pressure, "ppm": ppm}

    return json.dumps(message)