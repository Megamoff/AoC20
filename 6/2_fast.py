file = open("input", "r")

data = file.read()

s = 0
data = data.split("\n\n")
for x in data:
	x = x.split("\n")
	res = list(x[0])
	for i in x:
		delt = []
		for k in res:
			if k in i:
				delt.append(k)
		res = delt
	s += len(res)
print(s)
