#Tuples
#Ordered collection
#Immutable (cannot change after creation)
#Allows duplicate elements
#Elements can be of mixed data types
# A tuple of student information
student = ("John Doe", 20, "Computer Science")

# Accessing elements
print(student[0])  
print(student[1])  

# Trying to modify a tuple will raise an error
# student[1] = 21  # ❌ This will cause a TypeError (tuples are immutable)


#Set
#Unordered collection
#Mutable (you can add/remove items)
#No duplicate elements
#Cannot contain mutable items like lists or dictionaries
# A set of unique colors
colors = {"red", "blue", "green", "red"}

print(colors)  

# Add an element
colors.add("yellow")
print(colors)  

# Check membership
print("blue" in colors)  

# Remove an element
colors.remove("red")
print(colors)  
