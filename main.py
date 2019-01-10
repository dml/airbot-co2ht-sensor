from machine import Pin
import time
from umqtt.robust import MQTTClient


PIN = Pin(15, Pin.OUT)


def blink(delay):
    PIN.on()
    time.sleep_ms(delay)
    PIN.off()
    time.sleep_ms(delay)

client = MQTTClient(b"d02", b"192.168.0.81")
blink(500)
client.connect()
blink(500)

while True:
    blink(1000)
    client.publish(b"sensors/d02/temperature", b'{"source": "d02", "value": 10.33}')

client.disconnect()
