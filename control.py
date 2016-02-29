import projector_control
import rxvc.cache as cache
import time

mappings = {
    'desktop':4,
    'wiiu':5,
    'rpi':2
}

def get_receiver():
    receiver = cache.find_receiver()
    return receiver


def set_input(inp):
    if inp in mappings:
        projector_control.set_power(True)
        get_receiver().on = True
        time.sleep(5)
        get_receiver().input = 'HDMI%d' % (mappings[inp],)


def off():
    projector_control.set_power(False)
    get_receiver().on = False
