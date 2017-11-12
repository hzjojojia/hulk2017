#with open('pi_digits.txt') as file_object:
#	contents = file_object.read()
#	print (contents)
	


file_name = 'pi_digits.txt'
with open(file_name) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
