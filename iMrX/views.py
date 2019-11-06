from paho.mqtt import client as mqtt
from iMrX.setting import MqttHost,MqttPort,RecvTopic
from threading import Thread

client = None

def run(arg):
    arg.connect(MqttHost, MqttPort, 60)
    arg.subscribe(RecvTopic)
    arg.on_message = __message
    arg.loop_forever()

def __message(lient, data, msg):
    print(msg.topic + " " + ":" + str(msg.payload))

if client is None:
    client = mqtt.Client()
    MqttThread = Thread(target=run,args=(client,))
    MqttThread.start()


