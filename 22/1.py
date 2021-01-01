file = open("input")

data = file.read().split("\n\n")
deck1 = data[0].split("\n")[1: ]
deck2 = data[1].split("\n")[1: -1]

for i in range(len(deck1)):
	deck1[i] = int(deck1[i])
for i in range(len(deck2)):
	deck2[i] = int(deck2[i])

while len(deck1) > 0 and len(deck2) > 0:
	c1 = deck1[0]
	c2 = deck2[0]

#	print(c1 + " " + c2)

	deck1 = deck1[1: ]
	deck2 = deck2[1: ]

	if c1 > c2:
		deck1.append(c1)
		deck1.append(c2)
	else:
		deck2.append(c2)
		deck2.append(c1)
#	print(deck2)

for i in range(len(deck1)):
	deck1[i] = deck1[i]*(len(deck1)-i)
for i in range(len(deck2)):
	deck2[i] = deck2[i]*(len(deck2)-i)

print(sum(deck1))
