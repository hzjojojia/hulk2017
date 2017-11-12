print ("Give me two numbers, and I'll divide them.")
print ("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number:")
	if first_number == 'q':
		break
	second_number = input("\nSecond number:")
	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You cat not divide by zero!")
	else:
		print(answer)
