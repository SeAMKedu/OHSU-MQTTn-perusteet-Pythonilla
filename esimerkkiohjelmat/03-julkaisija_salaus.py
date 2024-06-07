import time
import json
import random
import paho.mqtt.client as mqtt 

# Tiedot
BROKER_ADDRESS = "KLUSTERIN_URL_TÄHÄN!!!"
USERNAME = "Python"
PASSWORD = "V3n0m0u5"
CLIENT_ID = "EsimerkkiJulkaisija"
TOPIC = "tuotantotila/pmxmittaus"
QOS = 0

# Callback-funktio, jonka liipaisee CONNACK-vastaus
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Otettiin yhteys välityspalvelimeen {BROKER_ADDRESS} koodilla {reason_code}")

# Callback-funktio, jonka liipaisee PUBACK-vastaus
def on_publish(client, userdata, message_id, reason_code, properties):
    print(f"Viesti lähetettiin id:llä {message_id}")

# Callback-funktio, jonka liipaisee uuden lokiviestin kirjoittaminen
def on_log(client, userdata, level, msg):
    print(msg)

# Luodaan uusi asiakas ja sidotaan callback-funktiot
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID, protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_publish = on_publish
client.on_log = on_log

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER_ADDRESS, port=8883)
print("ok")

# Aloitetaan julkaisusilmukka
client.loop_start()

try:
    while True:
        # Luodaan keinotekoinen mittauspiste
        measurement = {
            "pressure": 1024 + random.uniform(-2, 2),
            "temperature": 22 + random.uniform(-3, 3),
            "humidity": 33 + random.uniform(-2, 2) 
        }
        # muunnetaan json-muotoon ja julkaistaan MQTT-välityspalvelimella
        data = json.dumps(measurement)
        client.publish(TOPIC, data, QOS)
        time.sleep(1)
except KeyboardInterrupt:
    print("Katkaistaan yhteys välityspalvelimeen..")

client.loop_stop()
client.disconnect()
print("Yhteys katkaistu.")