file = open("input", "r")

input = file.read().split("\n")
grid = {}

for i in range(len(input)):
	for k in range(len(input[i])):
		if input[i][k] == "#":
			grid[(k, i, 0)] = True

def cycle():
	global grid
	new = {}
	check = {}
	for i in grid:
#		print()
#		print(i)
		res = -1
		for x in range(i[0] -1, i[0] +2):
			for y in range(i[1] -1, i[1] +2):
				for z in range(i[2] -1, i[2] +2):
#					print(str(x) + " " + str(y) + " " + str(z) + ": " + str(grid.get((x, y, z), False)))
					if grid.get((x, y, z), False):
						res +=1
					else:
						check[(x, y, z)] = True
		if res == 3 or res == 2:
			new[i] = True

	for i in check:
		res = 0
		for x in range(i[0] -1, i[0] +2):
			for y in range(i[1] -1, i[1] +2):
				for z in range(i[2] -1, i[2] +2):
					if grid.get((x, y, z), False):
						res +=1
		if res == 3:
			new[i] = True
	grid = new
	
for i in range(6):
	cycle()

print(len(grid))
