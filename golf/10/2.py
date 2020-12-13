file = open("input", "r")

data = []
for line in file:
	data.append(int(line))
data.append(0)
data = sorted(data)

def rec(start):
	sub = data[start: len(data)]
	if len(sub) == 1:
		return 1
	res = 0
	for i in range(1, 4):
		if i > len(sub) -1:
			break
		if sub[i] > sub[0] +3:
			break
		res += rec(start +i)
	return res

poss = []
for i in data:
	poss.append(0)
poss[-1] = 1

for i in range(len(data) +1, -1, -1):
	res = 0
	for k in range(1, 4):
		if i+k > len(data) -1:
			break
		if data[i+k] > data[i] +3:
			break
		poss[i] += poss[i+k]

print(poss)
