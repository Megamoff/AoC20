file = open("input", "r")

data = []
for line in file:
	data.append(line)
data = data[1].replace("\n", "").split(",")

counter = 4468048
found = True
while found:
	counter +=14948149
	if not (counter +56) % 37 == 0:
		continue
	if not (counter +48) % 29 == 0:
		continue
	if not (counter) % 19 == 0:
		continue
	print(counter)
	for i in range(len(data)):
		if data[i] == "x":
			continue
		if not (counter + i) % int(data[i]) == 0:
			break
		if i == len(data) -1:
			found = False
print(counter)
