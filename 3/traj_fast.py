file = open("input", "r")

map = file.read().split("\n")[: -1]

def slope (x, y):
	x = x/y
	count = 0
	for i in range(0, len(map), y):
		if map[i][int(i*x) % 31] == "#":
			count += 1
	return count

print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))
