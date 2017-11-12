cars = ['audi','bmw','subaru','toyata']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

request_topping = ['mushrooms','onions','pineapple']
topping1 = 'mushrooms1'
if topping1 not in request_topping:
	print(topping1.title() + ",It is not in.")
#	if 'mushrooms' in request_topping:
#		print(request_topping(0))
#	if'pepperoni' in request_topping:
#		print(true)

