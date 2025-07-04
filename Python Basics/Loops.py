#for-Loop
#The for loop is a fundamental control flow statement in Python that is used for iterating over a sequence (such as a list, tuple, string, or range) or other iterable objects.

#for loop with list
l = ["Data", "Science", "Python"]
for i in l:
	print(i)

#for loop with dictionary
print("Dictionary Iteration")
d = dict()

d['key1'] = "val1"
d['key2'] = 345
for i in d:
	print(i, d[i])

#for loop with string
word = "Python"

for letter in word:
    print(letter)

#for loop with Range
for i in range(5):
    print(i,end=' ')

#Enumerating using for loop
list1 = ["Data-Science", "Power BI", "Python"]

for index, subject in enumerate(list1):
    print(f"Index: {index}, Subj: {subject}")

### WHILE LOOP ###

outer_counter = 1
while outer_counter <= 3:
    inner_counter = 1
    while inner_counter <= 2:
        print(f"({outer_counter}, {inner_counter})", end=' ')
        inner_counter += 1
    outer_counter += 1

#While loop with break statement
counter = 1
while counter <= 10:
    print(counter,end=' ')
    if counter == 5:
        break
    counter += 1

#While loop with continue statement
counter = 1
while counter <= 5:
    if counter == 3:
        counter += 1
        continue
    print(counter, end=' ')
    counter += 1


## PROBLEM STATEMENT
#Problem Statement - Create a Python program that prompts the user to enter positive numbers continuously. 
#The program should use a while loop to collect input data until the user enters a non-positive number. 
#Implement simple data validation to ensure entered values are valid positive numbers. 
#Finally, output the list of positive numbers entered by the user. The objective is to create an interactive and error-tolerant program for collecting and handling user input.



numbers = []
​
while True:
    user_input = input("Enter a positive number (enter a non-positive number to stop): ")
​
    # Check if the input can be converted to a float and is non-negative
    if user_input.replace('.', '', 1).isdigit() and float(user_input) > 0:
        numbers.append(float(user_input))
    elif user_input.replace('-', '', 1).isdigit() and float(user_input) <= 0:
        break  # Exit the loop if a non-positive number is entered
    else:
        print("Invalid input. Please enter a valid positive number.")
​
# Data handling after the loop
if numbers:
    print(f"You entered the following positive numbers: {numbers}")
else:
    print("No positive numbers were entered.")
