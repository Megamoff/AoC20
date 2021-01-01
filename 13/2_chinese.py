file = open("input", "r")

data = []
for line in file:
	data.append(line)
data = data[1].replace("\n", "").split(",")

m = []
a = []
N = 1
n = []
X = 0

for i in range(len(data)):
	if data[i] == "x":
		continue
	m.append(int(data[i]))
	a.append(int(data[i]) - i)
	N *= int(data[i])

for i in m:
	n.append(int(N/i))

for i in range(len(m)):
	for k in range(1, m[i]):
		if k*n[i] % m[i] == 1:
			X += a[i]*k*n[i]
			break

while X > N:
	X -= N

print(X)
