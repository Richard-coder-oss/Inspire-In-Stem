#lists- a bunch of data that has been put together. variables that contain lists
# Working with lists
#Loops - while, for
#functions

#box brackets [ ] when you want to store the list
# Parenthesis { }
#calibraces ( )

#cities = ['Nai', 'Nak', 'Kis'] access items in the list using indeces
#indexes  [ 0         1      2] We begin listing at index 0

#python is case sensitive, space sensitive
# variables don't have spaces - e.g first_name="ada" (use underscore)
#variables must have meaning - e.g colors = "red"
# Variables can't begin with a number-(1name) but can have (name1)

#learning about lists
motorcycle_owner= "Richard Miruka"
plate_number=['H1234', 'Y1234', 'S1234']
motorcycle = [ 'honda', 'yamaha', 'suzuki']
#print(motorcycle)
motorcycle[0]= "Bugati" #changing element in a list
print(motorcycle[1])
#adding element in a list
motorcycle.append ('Bugatti') #adding item into a list.
print(motorcycle)
print(plate_number)
#deleting an item from a list --del
#del motorcycle[0] #deleting an item from a list
print(motorcycle)
popped_motorcycle=motorcycle.pop()
print(motorcycle)
#print a statement: My name is Richard Miruka and I own a motorcycle plate number
#print ('my name is ' + str(motorcycle_owner) + ' and i own a motorcycle' + ' plate number' + str(plate_number))
print

#remove statement- removing an item from a list
motorcycle.remove('yamaha')
print(motorcycle)

number_plate= ['H123', 'Y123', 'Z123']
motorcycle ['yamaha', 'suzuki', 'honda']

print(motorcycle)