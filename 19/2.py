import re

file = open("input")

input = file.read().split("\n\n")
rules = {}
msg = input[1].split("\n")[: -1]
input = input[0].split("\n")
valid = []

for i in input:
	num = i[: i.index(":")]
	rule = i[i.index(" "): ] + " "
	rules[num] = rule.replace("\"", "")
rules["8"] = " 42 + "
rules["11"] = " 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31 | 42 42 42 42 42 42 31 31 31 31 31 31"

for x in range(10):
	for i in rules:
		old = " " + i + " "
		new = rules[i]
		if "|" in new:
			new = " (" + new + ") "
		for k in rules:
			rules[k] = rules[k].replace(old, new)

for x in range(10):
	for i in rules:
		old = " " + i + " "
		new = rules[i]
		if "|" in new:
			new = " (" + new + ") "
		for k in rules:
			rules[k] = rules[k].replace(old, new)

for i in msg:
	exp = "^" + rules["0"].replace(" ", "") + "$"
	res = re.search(exp, i)
	if not res == None:
		valid.append(i)

print(len(valid))
