import time
#import publish, mqtt, measure

def wifi():
    from Backups import Wifi
    try:
        Wifi.connect()
        print("Wifi connected")
    except:
        print("Wifi connection failed")
    try:
        Wifi.synchronize_rtc()
        print("RTC synchronized")
    except:
        print("RTC synchronizing failed")


try:
    print("Connecting to Wifi and synchronizing RTC")
    Wifi()
    print("Connecting MQTT")
    mqtt_client = mqtt.connect_mqtt()
    print("MQTT connected")

    print("Publishing measured data")
    while True:
        publish.publish(mqtt_client, measure) # measured data
        time.sleep(5)
    print("Done")
except Exception as e:
    print(str(e))