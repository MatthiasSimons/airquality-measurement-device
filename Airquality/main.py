import get_data
import json
import time
import wifi
import mqtt

MQTT_TOPIC = "enter MQTT Topic"

def led(ppm):
    # set limit values
    low, medium, high = 200, 1000, 2000
    # led Pin config
    r_pin = Pin(14, Pin.OUT)  # d5
    g_pin = Pin(2, Pin.OUT)  # d4
    b_pin = Pin(0, Pin.OUT)  # d3
    
    frequency = 5000
    # led off
    r_pin.off()
    g_pin.off()
    b_pin.off()
    
    # set led color for limits
    if ppm < medium:
        r_pin.off()
        g_pin.on()
        b_pin.off()

    if ppm >= medium and ppm < high:
        r_pin.off()
        g_pin.off()
        b_pin.on()
     
    if ppm >= high:
        r_pin.on()
        g_pin.off()
        b_pin.off()

def measure_environment_data():
    # function for getting measured data
    return get_data.measure()


def publish_environment_data(mqtt_client):
    # publish data via mqtt
    message = measure_environment_data()
    ppm = message['ppm']
    # call led function for visual feedback
    led(ppm)
    # show measured data
    print(message)
    # publish measured data
    mqtt_client.publish(MQTT_TOPIC, json.dumps(message))


def connect_and_publish():
    # connect to wifi; sync time and publish data
    print("connect wifi and synchronize RTC")
    # establish wifi connection and synchronize time
    wifi.connect()
    wifi.synchronize_rtc()

    while True:
        # try to connect mqtt until succesful
        try:
            print("MQTT connect")
            mqtt_client = mqtt.connect_mqtt()
            time.sleep(1)
            break
        except:
            print("MQTT connection failed")
            time.sleep(1)

    print("start publishing data")
    while True:
        try:
            # publish data
            publish_environment_data(mqtt_client)
        except Exception as e:
            print(str(e))
        time.sleep(60)


connect_and_publish()
