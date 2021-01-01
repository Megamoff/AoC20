file = open("input", "r")

data = file.read().split("\n")[: -1]

def calculate(term):
	term = term.replace(" ", "")[1: -1]
	while "+" in term:
#		print(term)
		pos = term.index("+")
		begin = pos -1
		end = pos +1
		while begin > 0 and not term[begin -1] == "*":
			begin -= 1
		while end < len(term) and not term[end] == "*" and not term[end] == "+":
			end += 1
		sub = term[begin : end].split("+")
		res = int(sub[0]) + int(sub[1])
		term = term.replace(term[begin : end], str(res), 1)

	while "*" in term:
#		print(term)
		pos = term.index("*")
		begin = 0
		end = pos +1
		while end < len(term) and not term[end] == "*":
			end += 1
		sub = term[begin : end].split("*")
		res = int(sub[0]) * int(sub[1])
		term = term.replace(term[begin : end], str(res), 1)
#	print(term)

	return term#.strip()

for x in range(len(data)):
	i = data[x]
#	print()
#	print(i)
	while "(" in i:
		sub = i[: i.index(")") +1]
		last = len(sub) - sub[::-1].index("(") -1
		sub = sub[last: ]
		res = calculate(sub)
		i = i.replace(sub, res)
#		print(i)

	data[x] = int(calculate("(" + i + ")"))
#	print(data[x])

print(sum(data))
