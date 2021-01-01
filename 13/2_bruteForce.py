file = open("input", "r")

data = []
for line in file:
	data.append(line)
data = data[1].replace("\n", "").split(",")

counter = 1
found = True
while found:
	counter +=1
	print(counter)
	for i in range(len(data)):
		if data[i] == "x":
			continue
		if not (counter + i) % int(data[i]) == 0:
			break
		if i == len(data) -1:
			found = False
print(counter)
