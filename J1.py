print("Please enter the last 4 digits of the phone number")
dig1 = input()
dig2 = input()
dig3 = input()
dig4 = input()


if dig1 == 8 or dig1 == 9:
	print("This number is associated with a telemarketer")
	print("Please ignore the call.")
if dig4 == 8 or dig4 == 9:
	print("This number is associated with a telemarketer")
	print("Please ignore the call.")
if dig2 == dig3:
	print("This number is associated with a telemarketer")
	print("Please ignore the call.")
else:
	print("This number is not associated with a telemarketer")
	print("You can answer the call.")