file = open("input", "r")

data = file.read().split("\n")[: -1]
for i in range(len(data)):
	data[i] = data[i].replace("F", "0")
	data[i] = data[i].replace("B", "1")
	data[i] = data[i].replace("L", "0")
	data[i] = data[i].replace("R", "1")
	data[i] = int(data[i], 2)
data = sorted(data)

for i in range(len(data) -1):
	if data[i]+1 != data[i+1]:
		print(data[i] +1)
