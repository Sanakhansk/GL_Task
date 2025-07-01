#Functions in python
#A function is a block of organized, reusable code that performs a specific task. 
# In python we use the 'def' keyword to define a function followed by a function name. 
# We can pass zero or more parameters within a function.

#creating and calling a function
def greet():
    print('Hello')

for i in range(5):
    greet()
    
#scope of variables
# Local Variable-A variable defined inside a function is local to that function and cannot be accessed outside of it.
# Global Variable-A variable defined outside of any function is global and can be accessed anywhere in the code.



#Function arguments
#Default Arguments-Default arguments are used to provide a default value for a parameter if no value is passed during the function call.
#Keyword Arguments-Keyword arguments allow you to pass arguments to a function by explicitly specifying the parameter names, making the code more readable and flexible.
def greet(name = '-----'):
    print('Hello from', name)

greet('GfG')
greet(name = 'GfG')
greet()

#keyword arguments
def student(firstname, lastname):
	print(firstname, lastname)

# Keyword arguments
student(firstname='Python', lastname='Programmer')
student(lastname='Programmer', firstname='Python')

#calling different functions together
lst = [1, 2, 3, 4, 5]

def sq(lst):
    return [i**2 for i in lst]

def cu(lst):
    return [i**3 for i in lst]

def final(lst):
    lst_1 = sq(lst)
    lst_2 = cu(lst)
    return [lst_1[i] + lst_2[i] for i in range(len(lst_1))]

print(final(lst))
