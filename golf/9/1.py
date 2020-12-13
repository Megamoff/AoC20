file = open("input", "r")

data = []
for line in file:
	data.append(int(line))

for i in range(25, len(data)):
	x = True
	for k in range(1, 26):
		for l in range(k +1, 26):
			if data[i] == data[i-k] + data[i-l]:
				x = False
	if x: #Work-around since python doesnt support continue/break of outer loop
		print(data[i])
		break
