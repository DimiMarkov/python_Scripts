import itertools

toDrawOnCurrentLine = 1
currentRow = 1


sizeOfObject = int(input())

numberOfCharInLastRow = sizeOfObject+(sizeOfObject-1)
whereToBegin = int(numberOfCharInLastRow / 2)

charsToDrawOnLine = sizeOfObject+(sizeOfObject-1)


while currentRow < sizeOfObject:

	toDrawOnCurrentLine = currentRow + (currentRow-1)
	whereToBegin -= 1
	line = 0
	while line < charsToDrawOnLine:
		line += 1
		if line == whereToBegin:
			for _ in itertools.repeat(None, toDrawOnCurrentLine):
				print('*', end='')
				line += 1
		else:
			print('.', end='')

		if line == charsToDrawOnLine - 1:
			print(end='\n')
	currentRow += 1
