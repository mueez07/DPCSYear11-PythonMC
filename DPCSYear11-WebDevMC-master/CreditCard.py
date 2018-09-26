cardstring = "49927398716"
length = len(card)
card = int(card)

def findSum(num):
	s = 0
	while num > 0:
		x = num % 10
		card = card % 10
		card = card//10
		s = s + x

		return s

def cardSum(card)
	#for i in range (length:
	#	if (length%2 == 0):
	ctr = 0
	for i in range (length):
		temp = cardstring[ctr:ctr+1]
		intsum = intsum + (temp*2)
		ctr = ctr + 2

cardsum(card)