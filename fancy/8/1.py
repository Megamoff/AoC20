file = open("input", "r")

prog = list()

for line in file:
	prog.append(line)

sp = 0
acc = 0
used = list()

while sp not in used:
	used.append(sp)
	command = prog[sp].split(" ")
	if command[0] == "acc":
		acc += int(command[1])
	elif command[0] == "jmp":
		sp += int(command[1]) -1
	sp += 1
print(acc)
