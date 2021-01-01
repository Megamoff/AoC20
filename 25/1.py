file = open("input")

data = file.read().split("\n")

door_public = int(data[0])
card_public = int(data[1])

door_ls = 0
card_ls = 0

s_number = 7

value = 1

while not value == door_public:
	value *= s_number
	value = value % 20201227
	door_ls += 1

key = 1
for i in range(door_ls):
	key *= card_public
	key = key % 20201227

print(key)	
