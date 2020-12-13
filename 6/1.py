file = open("input", "r")

input = ""

for line in file:
	input += line

s = 0
data = input.split("\n\n")
for x in data:
	x = x.replace("\n", "")
	x = set(x)
	s += len(x)

print(s)
