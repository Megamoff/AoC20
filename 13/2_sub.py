file = open("input", "r")
data = file.readlines()[1].replace("\n", "").split(",")

step = offset = 1
for i in range(len(data)):
	if data[i] == "x":
		continue
	while (offset + i) % int(data[i]) != 0:
		offset += step
	step *= int(data[i])

print(offset)
