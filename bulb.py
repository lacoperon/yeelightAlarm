import yeelight
import yeelight.transitions
import time
import random

bulb = yeelight.Bulb("192.168.1.83")
bulb.start_music()


bulb.set_brightness(random.random()*100)
flow = yeelight.Flow(
    count=1,
    transitions=yeelight.transitions.pulse(red=255, blue=0, green=255)
)

bulb.start_flow(flow)
