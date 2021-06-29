# Airquality
 IoT-Project for module "Industrielle Produktion und Industrie 4.0" @ FH Aachen

# Setup
create a cert folder and add cert.der, private.der and wifi_passwds.txt

in following files you need to set the variables

## main.py
MQTT_TOPIC = "enter MQTT Topic"

## mqtt.py
CERT_FILE = "cert file path"
KEY_FILE = "key file path"
MQTT_CLIENT_ID = "client id"
MQTT_HOST = "host link"

## wifi.py
wifi_passwds_path = "path to wifi_passwds.txt"

