current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1 


prompt = "\n Tell me something,and I will repeat it back to you:"
prompt = "\n Entet 'quit' to end the program."
message= ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)
	
prompt1 = "\n Tell me something,and I will repeat it back to you:"
prompt1 = "\n Entet 'quit' to end the program."	
active = True
while active:
	message = input(prompt1)
	if message == 'quit':
		active = False
	else:
		print(message)

current_number1 = 0
while current_number1 < 10:
	current_number1 += 1
	if current_number1  % 2 == 0:
		continue
	print(current_number1 )
