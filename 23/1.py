data = "215694783"
circle = []

for i in data:
	circle.append(int(i))


current = circle[0]
def round():
	global circle, current
	dest = current -1
#	print()
	print(circle)
	if dest == 0:
		dest = 9
	index = circle.index(current)
	if index > 5:
		pick = circle[index +1: ] + circle[: index -5]
		circle = circle[index -5: index +1]
	else:
		pick = circle[index +1: index +4]
		circle = circle[: index +1] + circle[index + 4: ]
#	print(current)
#	print(pick)
	while dest in pick:
		dest -= 1
		if dest == 0:
			dest = 9
	dest = circle.index(dest)
	circle = circle[: dest +1] + pick + circle[dest +1: ]
	index = circle.index(current)
	if index == len(circle) -1:
		index = -1
#	print(index)
	current = circle[index + 1]

for x in range(100):
	round()
print(circle)
