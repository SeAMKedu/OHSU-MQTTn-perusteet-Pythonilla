import paho.mqtt.subscribe as subscribe
from paho.mqtt.enums import MQTTProtocolVersion

BROKER_ADDRESS = "broker.hivemq.com"

def on_message_print(client, userdata, msg):
    print(f"viesti vastaanotettu: {msg.payload.decode('utf-8')}")
    print(f"viestin aihe: {msg.topic}")
    print(f"viestin laatutaso: {msg.qos}")
    print(f"viestin säilytyslippu: {msg.retain}")
    print(f"viestin id: {msg.mid}")
    userdata.append(msg)
    if len(userdata) >= 5:
        # Katkaistaan yhteys 5 vastaanotetun viestin jälkeen
        print("Riittävä määrä viestejä vastaanotettu.")
        print("Katkaistaan yhteys välityspalvelimeen...")
        client.disconnect()
        print("Yhteys katkaistu.")

subscribe.callback(on_message_print, 
                   "tuotantotila/pmxmittaus", 
                   hostname=BROKER_ADDRESS, 
                   userdata=[],
                   protocol=MQTTProtocolVersion.MQTTv5)
		
		
		
		
