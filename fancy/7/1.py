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
	rules[i] = rules[i].replace("no other", "")
	rules[i] = rules[i].replace(",", " , ")
	tmp = ''.join([k for k in rules[i] if not k.isdigit()])
	rules[i] = tmp

for i in range(len(rules)):
	colour = (rules[i])[0 : rules[i].index(":")]
	for k in range(len(rules)):
		rules[k] = rules[k].replace(colour, str(i))

for i in range(len(rules)):
	rules[i] = rules[i][rules[i].index(":"): ]
print(rules)

possible = [306]
for i in range(10):
	new = []
	for k in possible:
		for l in range(len(rules)):
			if " " + str(k) + " " in rules[l]:
				new.append(l)
	possible = list(set(possible + new))

print(len(possible))
