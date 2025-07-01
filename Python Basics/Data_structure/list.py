### LISTS IN PYTHON ###


#Ordered
#Mutable (can change values)
#Allows duplicate elements
#Can store any data type (integers, strings, lists, etc.)

#creating list
# creating a student_info list to store the information about the student roll no,name, course and marks scored
Student_info = [21, 'Rose', "CSE", 30, 40, 50]
print(Student_info)

#Accessing elements in a list
Student_info = [21, 'Rose', "CSE", 30, 40, 50, 120]
print("Student_roll :", Student_info[0], end=' , ')
print("Student_name :", Student_info[1], end=', ')
print("Student_totalMarks :", Student_info[-1], end=' ')

# Slicing a list
Student_info = [21, 'Rose', "CSE", 30, 40, 50, 120]
print(Student_info[1:3])

#reversing using slicing
Student_info = [21, 'Rose', "CSE", 30, 40, 50, 120]
print(Student_info[::-1])  # Reversed list
print(Student_info[::-2])  # Reversed list with steps of 2

#Modifying a list
Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student_info[2] = "ME"
print(Student_info)

# Adding elements to a list
Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student_info.append(50)
print(Student_info)

#removing elements from a list
Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student_info.remove(50)
print(Student_info)

#common methods in list

#concatenation of lists
Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student2_info = [22, "John", "ME", 40, 40, 50, 130]
print(Student_info + Student2_info)

#repetition of lists
Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
print(Student_info * 2)

#Iterating through a list


#1. Direct iteration
lst = [3, 5, 6, 5, 4, 3, 56, 8, 1]
for item in lst:
    print(item)
    
#2. Using index
for i in range(len(lst)):
    print(i, lst[i])
    
#3. Using reverse
for i in range(len(lst)-1, -1, -1):
    print(i, lst[i])
    


### MULTIDIMENSIONAL LISTS ###
List1= [ [1, 2, 3, 5], [4, 6, 7, 9], [8, 10, 11, 13] ]
#Accesing the rows of the list
for i in List1:
  print(i, end = ' -- ')
  
#Accessing each element of a 2D-list 
print("\n")
for i in range(len(List1)):
  for j in range(len(List1[i])):
                 print(List1[i][j], end=" , ")
                 
#Problem Statement - Finding maximum value in a 2 D list.
def find_max_value(matrix):
    max_value = float('-inf') 
    for row in matrix:
        max_value = max(max_value, max(row))
    return max_value

matrix = [
    [3, 7, 1, 2],
    [8, 5, 6, 4],
    [2, 1, 8, 9]
]
max_value = find_max_value(matrix)
print("\nMaximum Value:", max_value)

### List Comprehensions ###
# List comprehensions provide a concise way to create lists.
# They consist of brackets containing an expression followed by a for clause, and can also include optional
lst = [1, 2, 3, 4, 5, 6]
print(lst)
lst = [i**2 for i in lst]
print(lst)

