file = open("input", "r")

data = file.read().split("\n\n")

valid = 0
for i in range(len(data)):
	if "byr" not in data[i]:
		continue
	if "iyr" not in data[i]:
		continue
	if "eyr" not in data[i]:
		continue
	if "hcl" not in data[i]:
		continue
	if "ecl" not in data[i]:
		continue
	if "pid" not in data[i]:
		continue
	if "hgt" not in data[i]:
		continue
	valid +=1

print(valid)
