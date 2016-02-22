import serial
import time
import sys


def get_device():
    device='/dev/ttyUSB0'
    dev = serial.Serial()
    dev.port = device
    dev.baudrate = 19200
    dev.bytesize = 8
    dev.stopbits = 1
    dev.timeout = 3

    dev.open()
    dev.flush()

    time.sleep(3)

    return dev


def write_device(val):
    dev = get_device()
    dev.write(val)
    dev.flush()
    dev.close()

def set_power(turn_on):
    instruction = b'(PWR1)' if turn_on else b'(PWR0)'
    write_device(instruction)

def main():
    args = sys.argv
    handled = False
    if len(args) == 2:
        if args[1] == '1':
            set_power(True)
            handled=True
        elif args[1] == '0':
            set_power(False)
            handled=True

    return 0 if handled else 1


if __name__ == '__main__':
    sys.exit(main())
