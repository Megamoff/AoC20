input = open("input", "r")

for line in input:
	input2 = open("input", "r")
	for line2 in input2:
			if int(line)+int(line2)==2020:
				print(int(line)*int(line2))
