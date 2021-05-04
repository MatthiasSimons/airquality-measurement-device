from umqtt.robust import MQTTClient
import json
import time
from machine import Pin, I2C, RTC
import BME280
from MQ135 import MQ135

#
#400ppm – 750ppm: Good for health
#750 ppm – 1200 ppm: Take care
#1200 ppm (and above): Harmful to health

# The certificate and key file need to be converted from PEM to DER format first
#
#$ openssl x509 -in 1928794715-certificate.pem.crt -out cert.der -outform DER
#$ openssl rsa -in 1928794715-private.pem.key -out private.der -outform DER

CERT_FILE = "/cert/cert.der"
KEY_FILE = "/cert/private.der"

MQTT_CLIENT_ID = "ESP8266"
MQTT_PORT = 8883

MQTT_TOPIC = "Sensor1"

MQTT_HOST = "a17jeona196iam-ats.iot.eu-central-1.amazonaws.com"

def wifi():
    from Backups import Wifi
    Wifi.connect_wifi()
    Wifi.synchronize_rtc()

def convert_to_iso(datetime):
    y, m, d, _, h, mi, s, _ =  datetime
    return "{}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(y,m,d,h,mi,s)

def current_datetime():
    #iso_timestamp = convert_to_iso(RTC().datetime())
    return convert_to_iso(RTC().datetime())

def pub_msg(mqtt_client, msg):
    try:
        mqtt_client.publish(MQTT_TOPIC, msg)
        print("Sent: " + msg)
    except Exception as e:
        print("Exception publish: " + str(e))
        raise

def measure():
    #BME280
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)
    bme = BME280.BME280(i2c=i2c)

    temperature = bme.temperature.replace("C", "")
    humidity = bme.humidity.replace("%", "")
    pressure = bme.pressure.replace("hPa", "")

    temperature = float(temperature)
    pressure = float(pressure)
    humidity = float(humidity)

    #MQ135
    mq135 = MQ135(0) # analog PIN 0

    rzero = mq135.get_rzero()
    corrected_rzero = mq135.get_corrected_rzero(temperature, humidity)
    resistance = mq135.get_resistance()
    ppm = mq135.get_ppm()
    corrected_ppm = mq135.get_corrected_ppm(temperature, humidity)

    # print("temperature: ", temperature)
    # print("humidity: ", humidity)
    # print("ppm: ", corrected_ppm)

    return {"temperature": temperature, "humidity": humidity, "ppm": corrected_ppm,}

def measure_data_msg():
    try:
        message = measure()

    except Exception as e:
        message = {"error": "Error reading environment data: " + str(e)}
    return json.dumps(message)


def connect_mqtt(): #kann immer verwendet werden
    try:
        with open(KEY_FILE, "r") as f:
            key = f.read()

        print("Got Key")

        with open(CERT_FILE, "r") as f:
            cert = f.read()

        print("Got Cert")

        mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, server=MQTT_HOST, port=MQTT_PORT, keepalive=5000, ssl=True,
                                 ssl_params={"cert": cert, "key": key, "server_side": False})
        mqtt_client.connect()
        print('MQTT Connected')

        return mqtt_client

    except Exception as e:
        print('Cannot connect MQTT: ' + str(e))
        raise


try:
    print("Connecting to Wifi")
    wifi()
    print("Wifi connected")
    print("Connecting MQTT")
    mqtt_client = connect_mqtt()

    print("Publishing measured data")
    while True:
        #pub_msg(mqtt_client, create_dummy_msg()) # dummy Data
        pub_msg(mqtt_client, measure_data_msg()) # measured data
        time.sleep(5)
    print("Done")
except Exception as e:
    print(str(e))