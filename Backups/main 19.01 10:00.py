import time
#import publish, mqtt, measure
import network
import ntptime
import uos as os
from umqtt.robust import MQTTClient
from machine import Pin, I2C, RTC, ADC
import BME280
from MQ135 import MQ135

CERT_FILE = "/cert/cert.der"
KEY_FILE = "/cert/private.der"

MQTT_CLIENT_ID = "ESP8266"
MQTT_PORT = 8883

MQTT_TOPIC = "Sensor1"

MQTT_HOST = "a17jeona196iam-ats.iot.eu-central-1.amazonaws.com"

def publish(mqtt_client, msg):
    try:
        mqtt_client.publish(MQTT_TOPIC, msg)
        print("Sent: " + msg)
    except Exception as e:
        print("Exception publish: " + str(e))
        raise

def measureBME280():
    # BME280
    i2c = I2C(scl=Pin(5), sda=Pin(14), freq=10000)
    bme = BME280.BME280(i2c=i2c)

    temperature = float(bme.temperature.replace("C", ""))
    humidity = float(bme.humidity.replace("%", ""))
    pressure = float(bme.pressure.replace("hPa", ""))
    return temperature, humidity#, pressure


def measureMQ135(temperature=20., humidity=25.):
    # MQ135
    mq135 = MQ135(0)  # analog PIN 0
    temperature = 20.
    humidity = 25.
    #temperature, humidity = measureBME280()
    #temperature, humidity = float(temperature), float(humidity)
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

    # try:
    #     ppm = measureMQ135(temperature, humidity)
    #
    # except Exception as e:
    #     print('Cannot read MQ135: ' + str(e))

    message = {"datetime": timestamp, "temperature": temperature, "humidity": humidity, "pressure": pressure, "ppm": ppm}

    return json.dumps(message)

def connect_mqtt():
    try:
        with open(KEY_FILE, "r") as f:
            key = f.read()

        print("Got Key")

        with open(CERT_FILE, "r") as f:
            cert = f.read()

        print("Got Cert")

        try:
            print("test1")
            mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, server=MQTT_HOST, port=MQTT_PORT, keepalive=5000, ssl=True,
                                     ssl_params={"cert": cert, "key": key, "server_side": False})
            print("test2")
            mqtt_client.connect()
            print("test3")

        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, server=MQTT_HOST, port=MQTT_PORT, keepalive=5000,
                                     ssl=True,
                                     ssl_params={"cert": cert, "key": key, "server_side": False})
            mqtt_client.connect()

        print('MQTT Connected')

        return mqtt_client

    except Exception as e:
        print('Cannot connect MQTT: ' + str(e))
        raise

def connect_wifi():
    # wifi_passwds = {}
    #
    # with open("/cert/wifi_passwds.txt") as f:
    #     for line in f.readlines():
    #         wifi_id, passwd = line.strip().split(":")
    #         wifi_passwds[wifi_id] = passwd

    WIFI_SSID = "FRITZ!Box 7530 XU"
    WIFI_PW = "Simons_Wlan_2020"

    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        wlan.active(True)
        print('connecting to network', WIFI_SSID)
        wlan.connect(WIFI_SSID, WIFI_PW)
        while not wlan.isconnected():
            pass

    print("connected:", wlan.ifconfig())


def synchronize_rtc():
    # set the rtc datetime from the remote server
    ntptime.settime()
    print("rtc synchronized")


try:
    print("Connecting to Wifi and synchronizing RTC")
    try:
        connect_wifi()
        time.sleep(5)
    except Exception as e:
        print("Wifi connection failed")
        print(str(e))
    try:
        synchronize_rtc()
    except:
        print("synchronizing failed")
    time.sleep(5)
    print("Connecting MQTT")
    mqtt_client = connect_mqtt()
    time.sleep(5)
    print("MQTT connected")

    print("Publishing measured data")
    while True:
        try:
            publish(mqtt_client, measure()) # measured data
            time.sleep(5)
        except KeyboardInterrupt:
            pass

    print("Done")
except Exception as e:
    print(str(e))