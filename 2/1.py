file = open("input", "r")

valid = 0
for line in file:
	min = int(line[0: line.index("-")])
	max = int(line[line.index("-") +1: line.index(" ")])
	char = line[line.index(" ") +1: line.index(":")]
	word = line[line.index(":") +2: -1]
	count = word.count(char)
	if count <= max and count >= min:
		valid +=1
print(valid)
