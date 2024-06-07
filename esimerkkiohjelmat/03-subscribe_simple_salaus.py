import ssl
import paho.mqtt.subscribe as subscribe
from paho.mqtt.enums import MQTTProtocolVersion

BROKER_ADDRESS = "KLUSTERIN_URL_TÄHÄN!!!"
USERNAME = "Python"
PASSWORD = "V3n0m0u5"
tls_settings = {"tls_version": ssl.PROTOCOL_TLS}

try:
    msg = subscribe.simple("tuotantotila/pmxmittaus", 
                           hostname=BROKER_ADDRESS,
                           port=8883,
                           auth={"username": USERNAME, "password": PASSWORD},
                           tls=tls_settings,
                           protocol=MQTTProtocolVersion.MQTTv5)
    print(f"viesti vastaanotettu: {msg.payload.decode('utf-8')}")
    print(f"viestin aihe: {msg.topic}")
    print(f"viestin laatutaso: {msg.qos}")
    print(f"viestin säilytyslippu: {msg.retain}")
    print(f"viestin id: {msg.mid}")
except Exception as e:
    print(f"Tilauksessa tapahtui poikkeus: {e}")

