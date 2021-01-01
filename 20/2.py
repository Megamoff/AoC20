import random
file = open("photo")

img = file.read().split("\n")[: -1]

nessie = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
number_per_nessie = 15

def search():
	counter = 0
	for i in range(len(img) -3):
		for k in range(len(img[i]) -19):
			monster = True
			for l in range(len(nessie)):
				if not monster:
					break
				for m in range(len(nessie[l])):
					if nessie[l][m] == " ":
						continue
					if i+l >= len(img) or k+m >= len(img[0]):
						monster = False
						continue
					if not img[i +l][k +m] == nessie[l][m]:
						monster = False
						break
			if monster:
				counter += 1
#				for l in range(len(nessie)):
#					new = img[i +l]
#					for m in range(len(nessie[l])):
#						if nessie[l][m] == " ":
#							continue
#						new = new[: k +m] + "O" + new[k +m +1: ]
#					img[i +l] = new
	return counter



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

def rot(img):
	new = []
	for i in range(len(img[0])):
		line = ""
		for k in range(len(img)):
			line = line + img[k][i]
		new.append(line)
	return new

res = search()
for i in range(3):
	img = rot(img)
	res = search()
	if res > 0:
		break
if res == 0:
	img = flip_h(img)
	res = search()
	for i in range(3):
		img = rot(img)
		res = search()
		if res > 0:
			break

counter = 0
for i in img:
	counter += i.count("#")
#	print(i.replace(".","") + " " + str(i.count("#")))
#for i in range(len(img)):
#	for k in range(len(img[i])):
#		new = img[i]
#		if "#" == img[i][k]:
#			counter += 1
#			new = new[: k] + "X" + new[k +1: ]
#		img[i] = new
			

#for i in img:
#	print(i)
#print(res)
print(counter - (res * number_per_nessie))
