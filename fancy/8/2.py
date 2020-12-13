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
			return
		used.append(sp)
		command = x[sp].split(" ")
		if command[0] == "acc":
			acc += int(command[1])
		if command[0] == "jmp":
			sp += int(command[1]) -1
		sp +=1

for i in range(len(prog)):
	y = copy.deepcopy(prog)
	y[i] = y[i].replace("nop", "jmp")
	run(y)
for i in range(len(prog)):
	y = copy.deepcopy(prog)
	y[i] = y[i].replace("jmp", "nop")
	run(y)
