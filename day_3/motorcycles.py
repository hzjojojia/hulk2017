motorcycles = ['honda','yamaha','suzuki']
print (motorcycles)

#motorcycles[0] = 'ducati'
#print (motorcycles)

motorcycles.append('ducati')
print (motorcycles)

motorcycles2 = []
motorcycles2.append('ducati')
motorcycles2.append('honda')
motorcycles2.append('yamaha')
print (motorcycles2)

motorcycles2.insert(0,'suzuki')
print (motorcycles2)

del motorcycles[0]
print (motorcycles)

#popped_motorcycles = motorcycles.pop()
#print (motorcycles)
#print (popped_motorcycles)

#first_owned = motorcycles.pop(1)
#print (first_owned)

#del_yamaha
#motorcycles.remove('yamaha')
#print (motorcycles)

del_it = 'yamaha'
motorcycles.remove(del_it)
print (motorcycles)
print (del_it)



