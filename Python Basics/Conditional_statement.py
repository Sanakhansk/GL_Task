#if-else 
#Conditional statements are fundamental to programming as they allow the execution of specific code blocks based on certain conditions. 
# In Python, the if-else statement is a powerful tool for incorporating decision-making logic into your programs.

#if-else statements are used to execute a block of code if a specified condition is true.
i = 31
if (i < 25):
	print("i is smaller than 25 , this is if Block")
else:
	print("i is greater than 25, this is else Block")
print("out of if and else Block")


#else-if statements, also known as elif in Python, allow you to check multiple conditions sequentially.
x = 0

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
    
#Nested if-else statements allow you to check conditions within other conditions, providing a way to handle complex decision-making scenarios.
year = int(input("Enter a year: "))

# Check if it's a leap year
if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a leap year.")
    else:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year.")