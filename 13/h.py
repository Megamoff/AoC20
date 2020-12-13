file = open("input", "r")

data = []
for line in file:
	data.append(line)
data = data[1].replace("\n", "").split(",")

counter = 4468048
found = True
while found:
	counter +=14948149
	if (counter +9) % 41 == 0:
		print(counter)
