import serial
import time
import sys


def get_device():
    device='/dev/ttyUSB0'
    serial = serial.Serial()
    serial.port = device
    serial.baudrate = 19200
    serial.bytesize = 8
    serial.stopbits = 1
    serial.timeout = 3

    serial.open()
    serial.flush()

    time.sleep(3)

    return serial


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
