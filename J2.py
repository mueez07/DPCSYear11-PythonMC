n = int(input(""))
p1 = input("")
p2 = input("")

ctr = 0

for i in range(n):
	if (p1[i:i+1] == "C" ) and (p2[i:i+1] == "C"):
	ctr = ctr + 1

print(ctr)