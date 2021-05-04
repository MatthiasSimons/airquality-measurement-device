from umqtt.robust import MQTTClient

CERT_FILE = "/cert/cert.der"
KEY_FILE = "/cert/private.der"

MQTT_CLIENT_ID = "ESP8266"
MQTT_PORT = 8883

MQTT_TOPIC = "Sensor1"

MQTT_HOST = "a17jeona196iam-ats.iot.eu-central-1.amazonaws.com"

def connect_mqtt():
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