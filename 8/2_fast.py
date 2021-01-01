import copy

file = open("input", "r")

prog = list()

for line in file:
	prog.append(line)

def run(x):
	sp = 0
	acc = 0
	used = list()
	while sp not in used:
		if sp == len(prog):
			print(acc)
			return True
		used.append(sp)
		command = x[sp].split(" ")
		if command[0] == "acc":
			acc += int(command[1])
		if command[0] == "jmp":
			sp += int(command[1]) -1
		sp +=1

for i in range(len(prog)):
	if "acc" in prog[i]:
		continue
	if "nop" in prog[i]:
		y = copy.deepcopy(prog)
		y[i] = y[i].replace("nop", "jmp")
		if run(y):
			break
	else:
		y = copy.deepcopy(prog)
		y[i] = y[i].replace("jmp", "nop")
		if run(y):
			break
