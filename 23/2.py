data = "215694783"
cups = 10**6
steps = 1

class node:
	value = 0
	next = None
	def __init__(self, v, n):
		self.value = v
		self.next = n

marks = {}
last = node(cups, None)
marks[last.value] = last
prev = last
for i in range(cups -1, 0, -1):
	n = node(i, prev)
	prev = n
	if i % steps == 0:
		marks[int(i/steps)] = n
last.next = prev
first = prev
marks[0] = first


current = first
for i in range(len(data)):
	current.value = int(data[i])
	current = current.next
c = first
res = ""


current = first
for i in range(10**7):
#	print()
#	print(i +1)
	if i % 10000 == 0:
		print(i)
	pick = current.next
	end = pick.next.next
	current.next = end.next
	value = current.value -1

	sub_vals = [pick.value, pick.next.value, end.value]

	if value == 0:
		value = cups
	while value in sub_vals:
		value -= 1
		if value == 0:
			value = cups

	dest = marks[int(value/steps)]
#	if i == 250000:
#		steps *= 10
#	dest = first
	while not dest.value == value:
		dest = dest.next

	tmp = dest.next
	dest.next = pick
	end.next = tmp
	current = current.next

while not current.value == 1:
	current = current.next

for x in range(3):
	print(current.value)
	current = current.next

#for x in range(len(marks) -1):
#	res = res + str(c.value)
#	c = c.next
#print(res)
