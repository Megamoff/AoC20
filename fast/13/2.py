file = open("input", "r")

data = []
for line in file:
	data.append(line)
data = data[1].replace("\n", "").split(",")

step = 1
offset = 1

for i in range(len(data)):
	if data[i] == "x":
		continue
	while True:
		if (offset + i) % int(data[i]) == 0:
			break
		offset += step
	step *= int(data[i])

print(offset)
