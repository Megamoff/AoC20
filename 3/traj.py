file = open("input", "r")

map = []

i = 0
for line in file:
	map.append([])
	for j in range(0, 32):
		if line[j: j+1] == "#":
			map[i].append(1)
		else:
			map[i].append(0)
	i += 1

count = 0
for j in range(0, i):
	if map[1*j][(3*j) % 31]:
		count += 1
		print(count)
