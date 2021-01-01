file = open("input", "r")

s = 0
data = file.read().split("\n\n")
for x in data:
	s += len(set(x.replace("\n", "")))
print(s)
