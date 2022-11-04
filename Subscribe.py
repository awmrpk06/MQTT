import time
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print("Received: ")
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

#client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
#client.username_pw_set("awmrpk06", "1065287982aA")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("127.0.0.1", 1883)
# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("encyclopedia/#")
# you can also use loop_start and loop_stop
client.loop_forever()
