import time
import paho.mqtt.client as paho
from paho import mqtt
import random
# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

#client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
#client.username_pw_set("awmrpk06", "1065287982aA")
#last will mess
client.will_set("encyclopedia/status", "Sensor Disconnect", 0, False)
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("127.0.0.1", 1883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_publish = on_publish
#Will topic
client.publish("encyclopedia/status", "ONLINE")

# a single publish, this can also be done in loops, etc.
i = 0
while i < 8:
    time.sleep(1)
    temp =  random.randrange(25,35,1)
    client.publish("encyclopedia/temperature", payload= temp )
    print("Temp : ", temp)
    i = i + 1
client.disconnect()
print ("done")
