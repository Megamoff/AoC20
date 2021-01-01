data = [0,1,4,13,15,12,16]

for i in range(len(data), 2020):
	last = data[-1]
	if not last in data[: -1]:
		data.append(0)
		continue
	diff =  data[-2: : -1].index(last) +1
	data.append(diff)
print(data)
