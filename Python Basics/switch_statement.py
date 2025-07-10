def numbers_to_string(n):
    ones = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    if n == 1000:
        return "one thousand"
    words = ""
    if n >= 100:
        hundreds = n // 100
        words += ones[hundreds] + " hundred"
        n %= 100
        if n > 0:
            words += " and "

    if n >= 20:
        tens_place = (n // 10) * 10
        words += tens[tens_place]
        n %= 10
        if n:
            words += "-" + ones[n]
    elif n > 0:
        words += ones[n]
    elif words == "":
        words = "zero"
    return words


num = int(input("Enter a number between 0 and 1000: "))
if 1 <= num <= 1000:
    print(numbers_to_string(num))
else:
    print("Number out of range. Please enter a number between 0 and 1000.")
