file = open("input", "r")

seats = []
count = 0
for line in file:
	seats.append([])
	for i in line:
		if i != "\n":
			seats[count].append(i)
	count += 1

for x in range(2000):
	new = []
	for i in range(len(seats)):
		new.append([])
		for k in range(len(seats[i])):
			if seats[i][k] == ".":
				new[i].append(".")
				continue
			res = 0
			for l in range(i -1, i +2):
				if l < 0 or l > len(seats) -1:
					continue
				for m in range(k -1, k+2):
					if m < 0 or m > len(seats[l]) -1 or (l == i and m == k):
						continue
					if seats[l][m] == "#":
						res += 1
			if res == 0:
				new[i].append("#")
			elif res > 3:
				new[i].append("L")
			else:
				new[i].append(seats[i][k])
	if new == seats:
		break
	seats = new

s = 0
for i in seats:
	for k in i:
		if k == "#": s += 1
print(s)
