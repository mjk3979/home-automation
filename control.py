import projector_control
import rxvc.cache as cache
import time
import threading

mappings = {
    'desktop':4,
    'wiiu':5,
    'rpi':2
}

def get_receiver():
    receiver = cache.find_receiver()
    return receiver


def set_input_only(inp):
    if inp in mappings:
        get_receiver().input = 'HDMI%d' % (mappings[inp],)

def set_input(inp):
    if inp in mappings:
        projector_control.set_power(True)
        get_receiver().on = True
        get_receiver().input = 'HDMI%d' % (mappings[inp],)

        # If the amp is starting, wait 10 seconds and then send the input again
        threading.Timer(10, lambda: set_input_only(inp)).start()
        


def off():
    projector_control.set_power(False)
    get_receiver().on = False
