file = open("input", "r")

data = file.read().split("\n")[: -1]

def calculate(term):
	term = term[1: -1] + " "
	while "+" in term or "*" in term:
		num1 = int(term[: term.index(" ")])
		term = term[term.index(" ") +1: ]
		op = term[0]
		term = term[2: ]
		num2 = int(term[: term.index(" ")])
		term = term[ term.index(" ") +1: ]

		res = 0
		if op == "*":
			res = num1 * num2
		else:
			res = num1 + num2

		term = str(res) + " " + term
	return term.strip()

for x in range(len(data)):
	i = data[x]
	while "(" in i:
		sub = i[: i.index(")") +1]
		last = len(sub) - sub[::-1].index("(") -1
		sub = sub[last: ]
		res = calculate(sub)
		i = i.replace(sub, res)

	data[x] = int(calculate("(" + i + ")"))
#	print(str(i) + " " + str(len(str(i))))

print(sum(data))
