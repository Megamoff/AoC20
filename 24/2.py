file = open("input")

data = file.read().split("\n")[: -1]
grid = {}
neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]

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

def cycle():
	global grid
	new = {}
	check = {}
	for i in grid:
		res = 0
		for dx, dy in neighbors:
			x = i[0] + dx
			y = i[1] + dy
			if grid.get((x, y), False):
				res +=1
			else:
				check[(x, y)] = True
		if res == 1 or res == 2:
			new[i] = True

	for i in check:
		res = 0
		for dx, dy in neighbors:
			x = i[0] + dx
			y = i[1] + dy
			if grid.get((x, y), False):
				res +=1
		if res == 2:
			new[i] = True
	grid = new

for i in range(100):
	cycle()
print(len(grid))
