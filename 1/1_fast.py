file = open("input", "r")

data = []
for line in file:
	data.append(int(line))

for i in range(len(data)):
	for k in range(i +1, len(data)):
		if (data[i] + data[k] == 2020):
			print(data[i] * data[k])
