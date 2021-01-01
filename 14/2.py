file = open("input", "r")

prog = file.read().split("\n")[: -1]
mask = ""
mem = {}

def write(add, val):
#	for k in range(len(mem), add +1):
#		mem.append(0)
	mem[add] = val

for i in prog:
	if "mask" in i:
		mask = i[7: ]
		continue
	address = list(str(bin(int(i[4: i.index("]")]))[2: ]).zfill(len(mask)))
	val = int(i[i.index(" ") +3: ])
	for k in range(len(mask)):
		if mask[k] == "0":
			continue
		address[k] = mask[k]

	tmp = ""
	for k in address:
		tmp += k
	address = tmp

	for k in range(2 ** address.count("X")):
		x = str(bin(k)[2: ]).zfill(address.count("X"))
		add = list(address)
		for l in x:
			add[add.index("X")] = l

		tmp = ""
		for k in add:
			tmp += k
		add = int(tmp, 2)

		write(add, val)

print(sum(mem.values()))
