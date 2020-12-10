file = open("input", "r")

data = []
for line in file:
	data.append(int(line))
data = sorted(data)

one = 1
three = 1

for i in range(len(data) -1):
	if data[i] +1 == data[i+1]:
		one += 1
	elif data[i] +3 == data[i+1]:
		three += 1

print(one * three)
