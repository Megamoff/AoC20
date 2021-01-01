file  = open("input", "r")

data = file.read().split("\n\n")

notes = data[0].split("\n")
tickets = data[2].split("\n")[1: -1]
for i in range(len(tickets)):
	tickets[i] = tickets[i].split(",")

fields = {}

for i in notes:
	key = i[: i.index(":")]
	values = list()
	poss = i[len(key) +2:]
	poss = poss.split(" or ")
	poss2 = poss[0].split("-")
	for k in range(int(poss2[0]), int(poss2[1]) +1):
		values.append(k)
	poss3 = poss[1].split("-")
	for k in range(int(poss3[0]), int(poss3[1]) +1):
		values.append(k)
	fields[key] = values

#remove invalid tickets
valid = []
for i in fields:
	valid = valid + fields[i]
valid = list(set(valid))

ntickets = []
for i in tickets:
	val = True
	for k in i:
		if int(k) not in valid:
			val = False
			break
	if val:
		ntickets.append(i)
tickets = ntickets

#wich field can be what
possible = [[]] * len(tickets[0])

for i in fields:
	for k in range(len(tickets[0])):
		valid = True
		for l in range(len(tickets)):
			if not int(tickets[l][k]) in fields[i]:
				valid = False
		if valid:
			possible[k] = possible[k] + [i]

assign = {}

for x in possible:
	for i in range(len(possible)):
		if len(possible[i]) == 1:
			key = possible[i][0]
			assign[key] = i
			for k in range(len(possible)):
				if key in possible[k]:
					possible[k].remove(key)

my = data[1][data[1].index("\n") +1: ].split(",")
result = 1

for i in assign:
	if not "depart" in i:
		continue
	result *= int(my[assign[i]])

print(result)
