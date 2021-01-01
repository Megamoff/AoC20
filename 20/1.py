file = open("input")

data = file.read().split("\n\n")[: -1]

images = {}

for i in data:
	i = i.split("\n")
	number = int(i[0][-5: -1])
	images[number] = i[1: ]

borders = {}

for i in images:
	image = images[i]

	border = image[0]
	borders[str(i) + "t"] = border
	border = image[-1]
	borders[str(i) + "b"] = border

	border = ""
	for k in image:
		border = border + k[0]
	borders[str(i) + "l"] = border

	border = ""
	for k in image:
		border = border + k[-1]
	borders[str(i) + "r"] = border

adj = {}
for i in borders:
	if i in adj:
		adj[adj[i]] = i
		continue
	for k in borders:
		if i == k:
			continue
		if borders[i] == borders[k] or borders[i] == borders[k][::-1]:
			adj[k] = i
			continue
	adj[i] = ""

for i in adj:
#	if adj[i] == "":
		print(i + " = " + adj[i])
