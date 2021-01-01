file = open("input")

data = file.read().split("\n")[: -1]

for i in range(len(data)):
	data[i] = data[i].replace("(", "").replace(")","").replace(",", "")
	data[i] = data[i].split(" contains ")
	data[i][0] = data[i][0].split(" ")
	data[i][1] = data[i][1].split(" ")

allergens = set()
for i in data:
	for k in i[1]:
		allergens.add(k)

poss = {}
for i in allergens:
	food = []
	for k in data:
		if i in k[1]:
			food.append(k[0])
	poss[i] = food

for i in poss:
	x = poss[i]
	res = x[0]
	for l in x:
		delt = []
		for k in res:
			if k in l:
				delt.append(k)
		res = delt
	poss[i] = res

for x in range(len(poss)):
	for i in poss:
		if len(poss[i]) == 1:
			for k in poss:
				if i == k:
					continue
				if poss[i][0] in poss[k]:
					poss[k].remove(poss[i][0])
for i in poss:
	poss[i] = poss[i][0]

for i in range(len(data)):
	for k in poss:
		if poss[k] in data[i][0]:
			data[i][0].remove(poss[k])

sum = 0
for i in data:
	sum += len(i[0])
print(sum)
