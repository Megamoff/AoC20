import math

file = open("input", "r")

posX = 0
posY = 0
facing = 0

for line in file:
	instr = line[: -1]
	action = instr[0]
	value = int(instr[1: ])

	if action == "R":
		facing -= value
	elif action == "L":
		facing += value
	elif action == "N":
		posY += value
	elif action == "S":
		posY -= value
	elif action == "E":
		posX += value
	elif action == "W":
		posX -= value
	elif action == "F":
		posX += value * int(math.cos(math.radians(facing)))
		posY += value * int(math.sin(math.radians(facing)))

	print(str(posX) + " " + str(posY))

print(str(abs(posX) + abs(posY)))
