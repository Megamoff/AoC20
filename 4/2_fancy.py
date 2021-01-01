file = open("input", "r")

data = file.read().split("\n\n")

valid = 0
for i in range(len(data)):
	data[i] = data[i].replace("\n"," ")
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
	tmp = data[i].split(" ")
	p = {}
	for k in tmp:
		k = k.split(":")
		if len(k) == 2:
			p[k[0]] = k[1]

	if int(p["byr"]) > 2002 or int(p["byr"]) < 1920:
		continue
	if int(p["iyr"]) > 2020 or int(p["iyr"]) < 2010:
		continue
	if int(p["eyr"]) > 2030 or int(p["eyr"]) < 2020:
		continue
	if not "#" == p["hcl"][0] or not int(p["hcl"][1: ], 16):
		continue
	y = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	if p["ecl"] not in y:
		continue
	if len(p["pid"]) > 9 or not p["pid"].isnumeric():
		continue
	if "cm" in p["hgt"]:
		if int(p["hgt"][0: -2]) < 150 or int(p["hgt"][0: -2]) > 193:
			continue
	elif "in" in p["hgt"]:
		if int(p["hgt"][0: -2]) < 59 or int(p["hgt"][0: -2]) > 79:
			continue
	else:
		continue
	valid += 1

print(valid)
