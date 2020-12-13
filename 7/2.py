file = open("input", "r")

tmp = ""
for line in file:
	tmp += line
rules = tmp.split("\n")
del rules[-1]

for i in range(len(rules)):
	rules[i] = rules[i].replace(" bags", "")
	rules[i] = rules[i].replace(" bag", "")
	rules[i] = rules[i].replace(" ", "")
	rules[i] = rules[i].replace(".", " ")
	rules[i] = rules[i].replace("contain", ": ")
	rules[i] = rules[i].replace("noother", "")
	rules[i] = rules[i].replace(",", " , ")

for i in range(len(rules)):
	colour = (rules[i])[0 : rules[i].index(":")]
	for k in range(len(rules)):
		rules[k] = rules[k].replace(colour, "."+str(i))

for i in range(len(rules)):
	rules[i] = rules[i][rules[i].index(":") +2: ]

contains = list()
for i in range(len(rules)):
	contains.append(0)
check = list()
check.append("1.306")

for i in range(2000000):
	if i >= len(check):
		break
	bag = int(check[i][check[i].index(".") +1: ])
	count = int(check[i][ : check[i].index(".")])
	contains[bag] += count
	search = rules[bag].split(" , ")
	for k in search:
		if "." not in k:
			continue
		for y in range(count):
			check.append(k)
print(check)
print(contains)
	
sum = 0
for i in contains:
	sum += i
print(sum)
