import paho.mqtt.publish as publish
from paho.mqtt.enums import MQTTProtocolVersion
import json
import random

BROKER_ADDRESS= "broker.hivemq.com"

# Paine - lämpötila - kosteus-mittaus
measurement = {
    "pressure": 1024 + random.uniform(-2, 2),
    "temperature": 22 + random.uniform(-3, 3),
    "humidity": 33 + random.uniform(-2, 2) 
}

# Nestemittaukset
fluid_measurement = {
    "flow_rate": 100 + random.uniform(-5, 5),
    "ph": 8 + random.uniform(-0.5, 0.5)
}

# muunna json-muotoon ja lähetä MQTT brokerille
data1 = json.dumps(measurement)
data2 = json.dumps(fluid_measurement)

msgs = [{"topic": "tuotantotila/pmxmittaus", "payload": data1, "qos":0}, {"topic": "tuotantotila/nestemittaus", "payload": data2, "qos": 0}]

try:
    publish.multiple(msgs, 
                     hostname=BROKER_ADDRESS, 
                     protocol=MQTTProtocolVersion.MQTTv5)
    print("Viestit julkaistiin onnistuneesti")
except Exception as e:
    print(f"Viestejä julkaistaessa tapahtui poikkeus: {e}")

