import control
import os
import projector_control
import time

def wiiu_on():
	return os.system("ping -c 1 -t 2 192.168.2.5 > /dev/null 2> /dev/null") == 0

def main():
	on = False
	cooldown = False
	print("starting daemon")
	while True:
		if wiiu_on() and not on:
			control.set_input("wiiu")
			print("turning on")
			on = True
			cooldown = True
		elif (not wiiu_on()) and on:
			control.off()
			print("turning off")
			on = False
			cooldown = True
		if cooldown:
			time.sleep(30)
			cooldown = False
		else:
			time.sleep(1)

if __name__ == "__main__":
	main()
