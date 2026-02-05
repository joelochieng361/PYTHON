#python list
#A list in python is a collection of items that ordered in a certain way
#A list is introduced by the use of square brackets
#The items in a list are stored in indexes. We start counting from index zero in programing
#A list is mutable i.e the contents of a list can be changed

cars = ["BMW","BENZE","HIANCE","PRADO", "PROBOX", "MCLAREN", "RANGE"]

print(cars)
print(type(cars))

#accessing items in a list
print(cars[2])
print("the car on index fout is",[4])

#list slicing - this is creating a list from a bigger list
print(cars[4:])

#print from index zero to three
print(cars[:4])

#print from hiance to probox
print(cars[2:5])

#list - mutuability
#we use the functionappend to add items to a list
cars.append("MERCEDES")
print(cars)

cars.append("SUBARU")
print(cars)

#pop is used to remove items from a list
cars.pop()
print(cars)

cars[5] = "pajero"
print(cars)

# we use the sort function to sort items in alphabetical order
cars.sort()
print(cars)