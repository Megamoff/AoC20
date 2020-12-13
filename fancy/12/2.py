import math

file = open("input", "r")

sPosX = 0
sPosY = 0
wPosX = 10
wPosY = 1

for line in file:
	instr = line[: -1]
	action = instr[0]
	value = int(instr[1: ])

	if action == "R":
		if value == 90:
			h = -wPosX
			wPosX = wPosY
			wPosY = h
		if value == 180:
			wPosX = -wPosX
			wPosY = -wPosY
		if value == 270:
			h = -wPosY
			wPosY = wPosX
			wPosX = h
	elif action == "L":
		if value == 90:
			h = -wPosY
			wPosY = wPosX
			wPosX = h
		if value == 180:
			wPosX = -wPosX
			wPosY = -wPosY
		if value == 270:
			h = -wPosX
			wPosX = wPosY
			wPosY = h
	elif action == "N":
		wPosY += value
	elif action == "S":
		wPosY -= value
	elif action == "E":
		wPosX += value
	elif action == "W":
		wPosX -= value
	elif action == "F":
		sPosX += value * wPosX
		sPosY += value * wPosY

print(str(abs(sPosX) + abs(sPosY)))
