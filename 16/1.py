file  = open("input", "r")

data = file.read().split("\n\n")

fields = data[0].split("\n")
tickets = data[2].replace(",", "\n").split("\n")[: -1]

valid = set()
error = 0

for i in range(len(fields)):
	fields[i] = fields[i][fields[i].index(":") +2: ]
	fields[i] = fields[i].replace(" or ", "\n")
	fields[0] = fields[0] + "\n" + fields[i]

fields = fields[0]
fields = fields.split("\n")

for i in fields:
	i = i.split("-")
	for k in range(int(i[0]), int(i[1]) +1):
		valid.add(k)

for i in tickets:
	if "nearby" in i:
		continue
	if not int(i) in valid:
		error += int(i)

print(error)
