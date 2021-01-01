import copy

file = open("input")

data = file.read().split("\n\n")
deck1 = data[0].split("\n")[1: ]
deck2 = data[1].split("\n")[1: -1]

for i in range(len(deck1)):
	deck1[i] = int(deck1[i])
for i in range(len(deck2)):
	deck2[i] = int(deck2[i])

counter = 0
def play(d1, d2):
	global counter
	prev = []
	counter += 1
#	print(counter)
	while len(d1) > 0 and len(d2) > 0:
		if d1 in prev:
			return True
		prev.append(d1)
		c1 = d1[0]
		c2 = d2[0]

		d1 = d1[1: ]
		d2 = d2[1: ]

		if c1 <= len(d1) and c2 <= len(d2):
			if play(copy.deepcopy(d1)[: c1], copy.deepcopy(d2)[: c2]):
				d1.append(c1)
				d1.append(c2)
			else:
				d2.append(c2)
				d2.append(c1)
		elif c1 > c2:
			d1.append(c1)
			d1.append(c2)
		else:
			d2.append(c2)
			d2.append(c1)
	counter -=1
	return len(d2) == 0

def play_top(d1, d2):
	while len(d1) > 0 and len(d2) > 0:
		c1 = d1[0]
		c2 = d2[0]

		d1 = d1[1: ]
		d2 = d2[1: ]

		if c1 <= len(d1) and c2 <= len(d2):
			if play(copy.deepcopy(d1)[: c1], copy.deepcopy(d2)[: c2]):
				d1.append(c1)
				d1.append(c2)
			else:
				d2.append(c2)
				d2.append(c1)
		elif c1 > c2:
			d1.append(c1)
			d1.append(c2)
		else:
			d2.append(c2)
			d2.append(c1)
	return [d1, d2]

res = play_top(deck1, deck2)
deck1 = res[0]
deck2 = res[1]

print(deck1)
print(deck2)

for i in range(len(deck1)):
	deck1[i] = deck1[i]*(len(deck1)-i)
for i in range(len(deck2)):
	deck2[i] = deck2[i]*(len(deck2)-i)

print(sum(deck1))
print(sum(deck2))
