file = open("input", "r")

data = file.read().split("\n")[: -1]

for x in range(len(data)):

print(sum(data))
