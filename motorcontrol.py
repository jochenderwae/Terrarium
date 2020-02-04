#!/usr/bin/python3

import sys
from adafruit_motorkit import MotorKit

if len(sys.argv) != 5:
	print("supply 4 arguments, one for each motor to control");
	print(" the arguments can be on, off and left")
	sys.exit(1)


kit = MotorKit()
args = sys.argv

try:
	with open('/var/local/motorcontrol_data', 'r') as f: states = eval(f.read())
except OSError as e:
	states = [False, False, False, False]

if args[1] == "on":
	kit.motor1.throttle = 1.0
	states[0] = True
elif args[1] == "off":
	kit.motor1.throttle = 0
	states[0] = False

if args[2] == "on":
	kit.motor2.throttle = 1.0
	states[1] = True
elif args[2] == "off":
	kit.motor2.throttle = 0
	states[1] = False

if args[3] == "on":
	kit.motor3.throttle = -1.0
	states[2] = True
elif args[3] == "off":
	kit.motor3.throttle = 0
	states[2] = False

if args[4] == "on":
	kit.motor4.throttle = 1.0
	states[3] = True
elif args[4] == "off":
	kit.motor4.throttle = 0
	states[3] = False

with open('/var/local/motorcontrol_data', 'w') as f:f.write(repr(states))

print("motor 1 - {0}".format("on" if states[0] else "off"))
print("motor 2 - {0}".format("on" if states[1] else "off"))
print("motor 3 - {0}".format("on" if states[2] else "off"))
print("motor 4 - {0}".format("on" if states[3] else "off"))



sys.exit(0)
