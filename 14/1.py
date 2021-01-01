file = open("input", "r")

prog = file.read().split("\n")[: -1]
mask = ""
mem = []

for i in prog:
	if "mask" in i:
		mask = i[7: ]
		continue
	address = int(i[4: i.index("]")])
	value = ""
	val = str(bin(int(i[i.index(" ") +3: ]))[2:]).zfill(len(mask))
	for k in range(len(mask)):
		if not mask[k] == "X":
			value += mask[k]
		else:
			value += val[k]
	if "b" in value:
		print(val)
		print(mask)
		print(value)
		print()
	for k in range(len(mem), address +1):
		mem.append(0)
	mem[address] = value

for i in range(len(mem)):
	mem[i] = int(str(mem[i]), 2)

print(sum(mem))
