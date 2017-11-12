for value in range(1,5):
	print(value)

numbers = list(range(1,5))
print(numbers)

numbers2 = list(range(2,11,2))
print(numbers2)

#squares = []
#for value in range(1,11):
#	square = value**2
#	squares.append(square)
#print (squares)
#a=min(squares)
#print(a)
#b=max(squares)
#print(b)
#c=sum(squares)
#print(c)

squares = [value**2 for value in range(1,11)]
print(squares)
