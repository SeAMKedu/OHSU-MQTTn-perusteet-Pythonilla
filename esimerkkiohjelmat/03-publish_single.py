import paho.mqtt.publish as publish
import json
import random
from paho.mqtt.enums import MQTTProtocolVersion

BROKER_ADDRESS = "broker.hivemq.com"

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
                   protocol=MQTTProtocolVersion.MQTTv5)
    print("Viesti julkaistiin onnistuneesti")
except Exception as e:
    print(f"Viestiä julkaistaessa tapahtui poikkeus: {e}")