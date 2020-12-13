file = open("input", "r")

data = ""

for line in file:
	data += line

s = 0
data = data.split("\n\n")
for x in data:
	x = x.split("\n")
	print(x)
	res = list(x[0])
	for i in x:
		delt = []
		for k in res:
			if k not in i:
				delt.append(k)
		for k in delt:
			res.remove(k)
		print(res)
	s += len(res)
print(s)
