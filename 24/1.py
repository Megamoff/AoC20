file = open("input")

data = file.read().split("\n")[: -1]
grid = {}

for i in data:
	x = 0
	y = 0
	while len(i) > 0:
		if i[0] == "e":
			x += 1
			i = i[1: ]
		elif i[0] == "w":
			x -= 1
			i = i[1: ]
		elif i[: 2] == "se":
			y -= 1
			i = i[2: ]
		elif i[: 2] == "nw":
			y += 1
			i = i[2: ]
		elif i[: 2] == "ne":
			x += 1
			y += 1
			i = i[2: ]
		elif i[: 2] == "sw":
			x -= 1
			y -= 1
			i = i[2: ]
	if (x, y) in grid:
		del grid[(x, y)]
	else:
		grid[(x, y)] = True

print(len(grid))
