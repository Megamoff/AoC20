file = open("input", "r")

tmp = file.read()
rules = tmp.split("\n")[: -1]

for i in range(len(rules)):
	rules[i] = rules[i].replace(" bags", "")
	rules[i] = rules[i].replace(" bag", "")
	rules[i] = rules[i].replace(" ", "")
	rules[i] = rules[i].replace(".", " ")
	rules[i] = rules[i].replace("contain", ": ")
	rules[i] = rules[i].replace("noother", "")
	rules[i] = rules[i].replace(",", " ")
	tmp = ''.join([k for k in rules[i] if not k.isdigit()])
	rules[i] = tmp

for i in range(len(rules)):
	colour = (rules[i])[0 : rules[i].index(":")]
	for k in range(len(rules)):
		rules[k] = rules[k].replace(colour, str(i))
	rules[i] = rules[i][rules[i].index(":") +1: ]

possible = [306]
pos = 0
while True:
	if pos == len(possible):
		break
	for l in range(len(rules)):
		if " " + str(possible[pos]) + " " in rules[l] and l not in possible:
			possible.append(l)
	pos += 1
print(len(possible))
