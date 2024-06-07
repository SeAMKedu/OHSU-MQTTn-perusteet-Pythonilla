import paho.mqtt.subscribe as subscribe
from paho.mqtt.enums import MQTTProtocolVersion

BROKER_ADDRESS = "broker.hivemq.com"

try:
    msg = subscribe.simple("tuotantotila/pmxmittaus", 
                           hostname=BROKER_ADDRESS,
                           protocol=MQTTProtocolVersion.MQTTv5)
    print(f"viesti vastaanotettu: {msg.payload.decode('utf-8')}")
    print(f"viestin aihe: {msg.topic}")
    print(f"viestin laatutaso: {msg.qos}")
    print(f"viestin säilytyslippu: {msg.retain}")
    print(f"viestin id: {msg.mid}")
except Exception as e:
    print(f"Tilauksessa tapahtui poikkeus: {e}")

