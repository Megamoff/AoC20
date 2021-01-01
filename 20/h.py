file = open("input")

data = file.read().split("\n\n")[: -1]

images = {}

def flip_h(img):
	new = []
	for i in img:
		new.append(i[::-1])
	return new

def flip_v(img):
	new = []
	for i in range(len(img) -1, -1, -1):
		new.append(img[i])
	return new

for i in data:
	i = i.split("\n")
	number = int(i[0][-5: -1])
	images[number] = i[1: ]

def rot(img):
	new = []
	for i in range(10):
		line = ""
		for k in range(9, -1, -1):
			line = line + img[k][i]
		new.append(line)
	return new

img = images[2777]
img = rot(img)
#img = rot(img)
#img = rot(img)
img = flip_v(img)
#img = flip_h(img)

for i in img:
	print(i)
