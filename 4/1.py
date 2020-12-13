file = open("input", "r")

input = ""
for line in file:
	input += line

data = input.split("\n\n")

valid = 0
for i in range(len(data)):
	x = ""
	try:
		x = data[i].index("byr")
		x = data[i].index("iyr")
		x = data[i].index("eyr")
		x = data[i].index("hcl")
		x = data[i].index("ecl")
		x = data[i].index("pid")
		x = data[i].index("hgt")
		valid +=1
	except ValueError:
		pass

print(valid)
