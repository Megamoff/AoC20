data = [0,1,4,13,15,12,16]

prev = {}

for i in range(len(data) -1):
	prev[data[i]] = i +1

num = data[-1]
for i in range(len(data), 30000000):
	diff = 0
	if num in prev:
		diff = i -prev[num]
	prev[num] = i
	num = diff
print(num)
