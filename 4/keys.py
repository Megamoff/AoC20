import sys

file = open("input", "r")


input = ""
for line in file:
	input += line

data = input.split("\n\n")

valid = 0
for i in range(len(data)):
	data[i] = data[i].replace("\n"," ")
	data[i] += " "
	x = ""
	try:
		x = int(data[i][data[i].index("byr") +4: data[i].index(" ", data[i].index("byr"))])
		if x < 1920 or x > 2002:
			continue
		x = int(data[i][data[i].index("iyr") +4: data[i].index(" ", data[i].index("iyr"))])
		if x < 2010 or x > 2020:
			continue
		x = int(data[i][data[i].index("eyr") +4: data[i].index(" ", data[i].index("eyr"))])
		if x < 2020 or x > 2030:
			continue
		x = data[i][data[i].index("hcl") +4: data[i].index(" ", data[i].index("hcl"))]
		if len(x) != 7 or x.index("#") != 0 or int(x.replace("#", "0x"), 16) == -1:
			continue
		x = data[i][data[i].index("ecl") +4: data[i].index(" ", data[i].index("ecl"))]
		y = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
		if not x in y:
			continue
		x = data[i][data[i].index("pid") +4: data[i].index(" ", data[i].index("pid"))]
		if len(x) != 9 or int(x) == -1:
			continue
		x = data[i][data[i].index("hgt") +4: data[i].index(" ", data[i].index("hgt"))]
		if "in" in x:
			hgt = int(x[0: x.index("in")])
			if hgt < 59 or hgt > 76:
				continue
		elif "cm" in x:
			hgt = int(x[0: x.index("cm")])
			if hgt < 150 or hgt > 193:
				continue
		else:
			continue
		valid +=1
	except ValueError:
#		print(data[i])
#		import traceback
#		msg = str(sys.exc_info()[0]) + "\n"
#		msg = msg + str(sys.exc_info()[1]) + "\n"
#		msg = msg + str(traceback.format_exc())
#		print(msg)
		pass

print(valid)
