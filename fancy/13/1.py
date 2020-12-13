file = open("input", "r")

data = []
for line in file:
	data.append(line)
time = int(data[0])
data = data[1].replace("x,", "").replace("\n", "").split(",")

dept = []
for i in data:
	n = int(time/int(i)) +1
	next = int(i) *n
	dept.append(next -time)
print(data)
print(dept)
