input = open("input", "r")

for line in input:
	input2 = open("input", "r")
	for line2 in input2:
		input3 = open("input", "r")
		for line3 in input3:
			if (int(line)+int(line2)+int(line3)==2020):
				print(int(line)*int(line2)*int(line3))
