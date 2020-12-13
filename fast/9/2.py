file = open("input", "r")

data = []
for line in file:
	data.append(int(line))

for i in range(0, data.index(22477624) -1):
	for k in range(i +1, data.index(22477624)):
		test = data[i: k]
		if sum(test) > 22477624: #if the sum is larger than the target, adding more elements wont help. Wastly improves execution time
			break
		if sum(test) == 22477624:
			print(sorted(test))
