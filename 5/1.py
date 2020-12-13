file = open("input", "r")

data = []
for line in file:
	row = line[0: 7]
	row = row.replace("F", "0")
	row = row.replace("B", "1")
	row = int(row, 2)
	col = line[7: 10]
	col = col.replace("L", "0")
	col = col.replace("R", "1")
	col = int(col, 2)
	pos = row*8+col
	data.append(pos)
data = sorted(data)
print(data)
