import paho.mqtt.client as mqtt

# Tiedot
BROKER_ADDRESS= "KLUSTERIN_URL_TÄHÄN!!!"
USERNAME = "Python"
PASSWORD = "V3n0m0u5"
CLIENT_ID = "EsimerkkiTilaaja"
TOPIC = "tuotantotila/pmxmittaus"
QOS = 0

# Callback-funktio, jonka liipaisee CONNACK-vastaus
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Otettiin yhteys välityspalvelimeen {BROKER_ADDRESS} ja saatiin vastaus {reason_code}.")
    print(properties)
    if reason_code.is_failure:
        print("loop_start jatkaa yhdistämisyrityksiä.")
    else:
        # Tilaaminen on_connect()-funktion sisällä tarkoittaa, että 
        # tilaus uudistetaan mahdollisen yhteyden katkeamista 
        # seuranneen uudelleen yhdistämisen jälkeen.
        client.subscribe(TOPIC, QOS)

# Callback-funktio, jonka liipaisee SUBACK-kuittaus
def on_subscribe(client, userdata, message_id, rc_list, properties):
    print(f"Tilausviestin tunniste {message_id}, saatu kuittaus {rc_list}.")

# Callback-funktio, jonka liipaisee UNSUBACK-kuittaus
def on_unsubscribe(client, userdata, message_id, reason_code_list, properties):
    # Parametri 'reason_code_list' on olemassa vain MQTTv5:ssä.
    # MQTTv3:ssa kyseinen parametri on aina tyhjä, ja SUBACK-viestin vastaanotto
    # tarkoittaa sen onnistumista.
    if len(reason_code_list) == 0 or not reason_code_list[0].is_failure:
        print("Tilauksen peruutus onnistui")
    else:
        print(f"Välityspalvelin vastasi virheviestillä: {reason_code_list[0]}")
    client.disconnect()

# Callback-funktio, jonka liipaisee vastaanotettu PUBLISH-viesti
def on_message(client, userdata, msg):
    print(f"viesti vastaanotettu: {msg.payload.decode('utf-8')}")
    print(f"viestin aihe: {msg.topic}")
    print(f"viestin laatutaso: {msg.qos}")
    print(f"viestin säilytyslippu: {msg.retain}")
    print(f"viestin id: {msg.mid}")

# Asiakkaan luonti ja sitominen callback-funktioihin
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID, protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_message = on_message

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(USERNAME, PASSWORD)

# Yhteydenotto välityspalvelimeen
client.connect(BROKER_ADDRESS, port=8883, clean_start=False)


# Aloitetaan kuuntelusilmukka
client.loop_start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Katkaistaan yhteys välityspalvelimeen...")

client.loop_stop()
client.disconnect()
print("Yhteys katkaistu.")