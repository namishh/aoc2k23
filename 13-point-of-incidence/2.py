total = 0
def isSymmetrical_w_smudge(arr):
	if len(arr) <= 1:
		return False
	alreadySmudged = False
	for i in range(len(arr)//2):
		if arr[i] != arr[-i-1]:
			if not(alreadySmudged):
				check = checkAllSmudges(arr[i], arr[-i-1])
				if not(check):
					return False
				else:
					alreadySmudged = True
			else:
				return False
	if alreadySmudged:
		return True
	else:
		return False

def checkAllSmudges(top,bottom):
	for i in range(len(top)):
		temp = top.copy()
		if temp[i] == ".":
			temp[i] = "#"
		else:
			temp[i] = "."
		if temp == bottom:
			return True
	return False

def transposeArray(arr):
	return list(map(list, zip(*arr)))

def determineMirror(arr):
	for i in range(2):
		for rowNum in range(len(arr)):
			if (rowNum+1)*2 < len(arr):
				temp = isSymmetrical_w_smudge(arr[:(rowNum+1)*2])
			else:
				temp = isSymmetrical_w_smudge(arr[-((len(arr)-1)-rowNum)*2:])
			if temp:
				if i == 1:
					return rowNum + 1
				if i == 0:
					return (rowNum + 1) * 100
		arr = transposeArray(arr)

images = []
with open('inputs.txt', 'r') as textIn:
	im = []
	for line in textIn:
		if line != '\n':
			temp = []
			for char in line:
				if char != '\n':
					temp.append(char)
			im.append(temp)
		else:
			images.append(im)
			im = []
	images.append(im)

for image in images:
	total += determineMirror(image)

print(total)
