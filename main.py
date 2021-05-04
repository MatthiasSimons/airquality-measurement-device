import get_data
from machine import RTC, Pin, PWM
import json
import time

import wifi
import mqtt

MQTT_TOPIC = "environment-data"

# 400ppm – 750ppm: Good for health
# 750 ppm – 1200 ppm: Take care
# 1200 ppm (and above): Harmful to health

# def led(ppm):
#     low, medium, high = 200, 400, 800
#
#     r_pin = Pin(14, Pin.OUT)  # d5
#     g_pin = Pin(2, Pin.OUT)  # d4
#     b_pin = Pin(0, Pin.OUT)  # d3
#     frequency = 5000
#
#     r_pin.off()
#     g_pin.off()
#     b_pin.off()
#
#     if ppm >1000.:
#         r_pin.on()
#         g_pin.off()
#         b_pin.off()
#
#     else:
#         r_pin.on()
#         g_pin.on()
#         b_pin.on()

        # r_led = PWM(r_pin, frequency).duty(1024)
    # g_led = PWM(g_pin, frequency).duty(1024)
    # b_led = PWM(b_pin, frequency).duty(1024)
    #
    # if ppm < medium:
    #     r_led = PWM(r_pin, frequency).duty(0)
    #     g_led = PWM(g_pin, frequency).duty(1024)
    #     b_led = PWM(b_pin, frequency).duty(0)
    #
    # if ppm >= medium and ppm < high:
    #     r_led = PWM(r_pin, frequency).duty(0)
    #     g_led = PWM(g_pin, frequency).duty(0)
    #     b_led = PWM(b_pin, frequency).duty(1024)
    #
    # if ppm >= high:
    #     r_led = PWM(r_pin, frequency).duty(0)
    #     g_led = PWM(g_pin, frequency).duty(1024)
    #     b_led = PWM(b_pin, frequency).duty(0)

def convert_to_iso(datetime):
    y, m, d, _, h, mi, s, _ =  datetime
    return "{}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(y,m,d,h,mi,s)


def measure_environment_data():
    return get_data.measure()


def publish_environment_data(mqtt_client):
    message = measure_environment_data()
    ppm = message['ppm']
    #led(ppm)
    print(message)
    mqtt_client.publish(MQTT_TOPIC, json.dumps(message))


def connect_and_publish():
    print("connect wifi and synchronize RTC")
    wifi.connect()
    wifi.synchronize_rtc()

    while True:
        try:
            print("MQTT connect")
            mqtt_client = mqtt.connect_mqtt()
            time.sleep(1)
            break
        except:
            print("MQTT connection failed")


    print("start publishing data")
    while True:
        try:

            publish_environment_data(mqtt_client)
        except Exception as e:
            print(str(e))
        time.sleep(5)


connect_and_publish()