numbers = int(raw_input())
zeroes = 0
product = 1
inputList = []
for i in range(numbers):
	n = int(raw_input())
	inputList.append(n)
	if n == 0:
		zeroes += 1
	else:
		product *= n

if zeroes >= 2:
	outputList = [0] * numbers
elif zeroes == 1:
	 outputList = [product if n == 0 else 0 for n in inputList]
else:
	outputList = [product / n for n in inputList]

for n in outputList:
	print n
