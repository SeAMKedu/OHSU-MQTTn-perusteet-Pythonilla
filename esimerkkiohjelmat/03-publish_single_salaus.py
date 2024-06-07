import paho.mqtt.publish as publish
import ssl
import json
import random
from paho.mqtt.enums import MQTTProtocolVersion

BROKER_ADDRESS = "KLUSTERIN_URL_TÄHÄN!!!"
USERNAME = "Python"
PASSWORD = "V3n0m0u5"
tls_settings = {"tls_version": ssl.PROTOCOL_TLS}

measurement = {
        "pressure": 1024 + random.uniform(-2, 2),
        "temperature": 22 + random.uniform(-3, 3),
        "humidity": 33 + random.uniform(-2, 2) 
    }
# muunnetaan json-muotoon ja julkaistaan MQTT-välityspalvelimella
data = json.dumps(measurement)

try:
    publish.single("tuotantotila/pmxmittaus", 
                   data,
                   hostname=BROKER_ADDRESS,
                   port=8883,     
                   auth={"username": USERNAME, "password": PASSWORD},
                   tls=tls_settings,
                   protocol=MQTTProtocolVersion.MQTTv5)
    print("Viesti julkaistiin onnistuneesti")
except Exception as e:
    print(f"Viestiä julkaistaessa tapahtui poikkeus: {e}")