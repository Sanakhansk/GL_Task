#Creating Dictionary
# Dictionary is a collection of key-value pairs

#Unordered (as of Python 3.7+, maintains insertion order)
#Mutable
#Stores key-value pairs
#Keys must be unique
#Values can be any type, keys must be immutable (like strings, numbers, tuples)
Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = dict({1: 'Data', 2: 'Science', 3: 'Python'})
print("Dictionary with the use of dict() method: ")
print(Dict)

Dict = dict([(1, 'Data'), (2, 'Science')])
print("Dictionary with each item as a pair: ")
print(Dict)

#Modifying a Dictionary
Dict = {}
Dict['name'] = 'Rose'
Dict['age'] = 24
Dict['city'] = 'Gwalior'
Dict ['city'] = 'Jaipur'
print("Dictionary after adding/modifying elements: ")
print(Dict)

#modifying dict using update function
print("Dictionary after modifying elements through update:")
Dict.update({'age':26,'city':'Noida'})
print(Dict)


### Dictionary comprehension ##
# Creating a dictionary using dictionary comprehension
dct = {i: i**3 for i in range(1, 6)}
print(dct)