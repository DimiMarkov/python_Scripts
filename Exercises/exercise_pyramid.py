import itertools

toDrawOnCurrentLine = 0
currentRow = 0


sizeOfObject = int(input())

numberOfCharInLastRow =	sizeOfObject+(sizeOfObject-1)
whereToBegin = int(numberOfCharInLastRow / 2)

while currentRow<sizeOfObject:
	charToDraw = sizeOfObject+(sizeOfObject-1)
	toDrawOnCurrentLine =	currentRow + (currentRow-1)
	whereToBegin -= 1
	i =	0
	while i<charToDraw:

		if i==whereToBegin:
			for _ in itertools.repeat(None, toDrawOnCurrentLine):
				print('*', end='')
		else:
			print(' ', end='')
		i += 1
		if i == charToDraw-1:
			print(end='\n')
	currentRow += 1
