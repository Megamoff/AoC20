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

			for l in range(k +1, len(seats[i])):
				if seats[i][l] == ".":
					continue
				if seats[i][l] == "#":
					res += 1
				break

			for l in range(k -1, -1, -1):
				if seats[i][l] == ".":
					continue
				if seats[i][l] == "#":
					res += 1
				break

			for l in range(i +1, len(seats)):
				if seats[l][k] == ".":
					continue
				if seats[l][k] == "#":
					res += 1
				break

			for l in range(i -1, -1, -1):
				if seats[l][k] == ".":
					continue
				if seats[l][k] == "#":
					res += 1
				break

			for l in range(1, len(seats)):
				if i +l > len(seats) -1 or k +l > len(seats[i+l]) -1:
					break
				if seats[i +l][k +l] == ".":
					continue
				if seats[i +l][k +l] == "#":
					res += 1
				break

			for l in range(1, len(seats)):
				if i +l > len(seats) -1 or k < l:
					break
				if seats[i +l][k -l] == ".":
					continue
				if seats[i +l][k -l] == "#":
					res += 1
				break

			for l in range(1, len(seats)):
				if i < l or k +l > len(seats[i -l]) -1:
					break
				if seats[i -l][k +l] == ".":
					continue
				if seats[i -l][k +l] == "#":
					res += 1
				break

			for l in range(1, len(seats)):
				if i < l or k < l:
					break
				if seats[i -l][k -l] == ".":
					continue
				if seats[i -l][k -l] == "#":
					res += 1
				break

			if res == 0:
				new[i].append("#")
			elif res > 4:
				new[i].append("L")
			else:
				new[i].append(seats[i][k])
	if new == seats:
		break
	seats = new

s = 0
for i in seats:
	t = ""
	for k in i:
		if k == "#": s += 1
		t +=k
	print(t)
print(s)
