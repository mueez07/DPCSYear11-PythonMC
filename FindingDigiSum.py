	
def findSum(n):
#inconsequential change
	n = 720
	s = 0

	while n > 0:
		x = n % 10
		n = n // 10
		s = s + x

	return(s)

def checkHarshad(n):
	if n % findSum(n) == 0:
		return True
	return False

low = input()
low = int(low)
high = input()
high = int(high)


for i in range (low, high, 1):
	print(checkHarshad(i))