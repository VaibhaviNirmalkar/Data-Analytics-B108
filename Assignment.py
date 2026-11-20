# Q1 Check if a number is positive, negative, or zero.
 
# num = int(input("Enter your number:"))

# if num > 0:
#     print("Positive")

# elif num<0:
#     print("Negative")

# else:
#     print("Zero")



# Q2 Check whether a number is even or odd.

# num = int(input("Enter your number:"))

# if num%2==0 :
#     print("Even")

# else:
#     print("Odd")



#  Q3 Find the greater of two numbers.

# a = int(input("Enter your a number:"))
# b = int(input("Enter your b number:"))

# if a>b :
#     print("a is greater than b")

# elif a<b:
#     print("a is smaller than b")

# elif a == b:
#     print("Both are equal")



# Q4 Find the greatest of three numbers.

# a = int(input("Enter your a number:"))
# b = int(input("Enter your b number:"))
# c = int(input("Enter your c number:"))

# if a>b and a>c :
#     print("a is greater than b and c")

# elif b>a and b>c:
#     print("b is greater than a and c")

# elif c>a and c>b :
#     print("c is greater than a and b")

# else:
#     print("All are equal")



# Q5 Check if a person is eligible to vote (age ≥ 18).

# age = int(input("Enter your age:"))

# if age>=18:
#     print("eligible for voting")

# else:
#     print("not eligible for voting")



# Q6 Check whether a year is a leap year.


# year = int(input("Enter your year:"))

# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("The year is a leap year")

# else:
#     print("The year is not a leap year")



# Q7 Check if a character is a vowel or consonant.

# char = input("Enter your character:")

# if char == "A" or char=="E" or char == "I" or char=="O" or  char == "U" or char=="a" or char == "e" or char=="i" or char=="o" or char=="u":
#     print("Vowel")

# else:
#     print("Consonant")



# Q8 Check whether a number is divisible by 5 and 11.

# num = int(input("Enter your  number:"))

# if num%5==0:
#     print("Divisible by 5")

# elif num%11==0:
#     print("Divisible by 11")



# Q9 Check if a number is a multiple of both 3 and 7.

# num = int(input("Enter your  number:"))

# if num%3==0 and num%7==0:
#     print("Divisible by 3 and 7 both")

# else:
#     print("Not divisble by 3 and 7")



# Q10 Assign grades based on marks:
# 90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# Below 60: F

# grade = int(input("Enter your marks:"))

# if grade>=90 and grade<=100:
#     print("Grade A")

# elif grade>=80 and grade<90:
#     print("Grade B")

# elif grade>=70 and grade<80:
#     print("Grade C")

# elif grade>=60 and grade<70:
#     print("Grade D")

# else:
#     print("Grade F")



# Q11 Check if a character is uppercase or lowercase.

# char = input("Enter a character: ")

# if char.isupper():
#     print("Uppercase letter")

# elif char.islower():
#     print("Lowercase letter")

# else:
#     print("Not an alphabet")



# Q12 Find whether the entered alphabet is a vowel using if-elif.

# ch = input("Enter an alphabet: ")

# if ch == 'a':
#     print("Vowel")
# elif ch == 'e':
#     print("Vowel")
# elif ch == 'i':
#     print("Vowel")
# elif ch == 'o':
#     print("Vowel")
# elif ch == 'u':
#     print("Vowel")
# else:
#     print("Consonant")


# Q13 Check if three sides can form a triangle.

# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:
#     print("The sides can form a triangle")

# else:
#     print("The sides cannot form a triangle")



# Q14 Determine the type of triangle (Equilateral, Isosceles, Scalene).


# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:

#     if a == b and b == c and a == c:
#         print("Equilateral Triangle")

#     elif a == b or b == c or a == c:
#         print("Isosceles Triangle")

#     else:
#         print("Scalene Triangle")

# else:
#     print("Invalid Triangle")



# Q15 Find the largest among four numbers.

# a = int(input("Enter your a number:"))
# b = int(input("Enter your b number:"))
# c = int(input("Enter your c number:"))
# d = int(input("Enter your d number:"))

# if a>b and a>c and a>d :
#     print("a is greater")

# elif b>a and b>c and b>d :
#     print("b is greater")

# elif c>a and c>b and c>d :
#     print("c is greater")

# elif d>a and d>b and d>c :
#     print("d is graeter")

# else:
#     print("All are equal")



# Q16 Check whether a number is a three-digit number.

# num = int(input("Enter a number: "))

# if num >= 100 and num <= 999:
#     print("It is a three-digit number")

# else:
#     print("It is not a three-digit number")



# Q17 Calculate electricity bill using slab rates.
# Units consumed	Rate
# 0–100 units	₹2/unit
# 101–200 units	₹3/unit
# 201–300 units	₹5/unit
# Above 300 units	₹7/unit

# units = int(input("Enter electricity units: "))

# if units <= 100:
#     bill = units * 2

# elif units <= 200:
#     bill = units * 3

# elif units <= 300:
#     bill = units * 5

# elif units > 300:
#     bill = units * 7

# print("Total amount:Rs.",bill)



# Q18 Calculate income tax based on income slabs.
# Annual income	Tax rate
# ₹0 – ₹2,50,000 ->	0%
# ₹2,50,001 – ₹5,00,000 ->	5%
# ₹5,00,001 – ₹10,00,000 ->	20%
# Above ₹10,00,000 -> 30%

# income = int(input("Enter annual income: "))

# if income <= 250000:
#     bill = (income) * 0/100

# elif income <= 500000:
#     bill = (income) * 5/100

# elif income <= 1000000:
#     bill = (income) * 20/100

# elif income > 1000000:
#     bill = (income)  * 30/100

# print("Total tax:Rs.",bill)



# Q19 Check if a student passes (minimum 35 marks in each subject).

# sub1 = int(input("Enter marks in subject 1: "))
# sub2 = int(input("Enter marks in subject 2: "))
# sub3 = int(input("Enter marks in subject 3: "))

# if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
#     print("Student is Pass")

# else:
#     print("Student is Fail")



# Q20 Find whether a number is within a given range.


# num = int(input("Enter a number: "))

# if num >= 10 and num <= 50:
#     print("Number is within the given range")

# else:
#     print("Number is outside the given range")



# Q21 Build a simple calculator using if-elif-else (+, -, *, /).


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# op = input("Enter operator (+, -, *, /): ")

# if op == "+":
#     print("Addition:", a + b)

# elif op == "-":
#     print("Subtraction:", a - b)

# elif op == "*":
#     print("Multiplication:", a * b)

# elif op == "/":
#     if b != 0:
#         print("Division:", a / b)
#     else:
#         print("Cannot divide by zero")

# else:
#     print("Invalid operator")




# Q22 Check if a year is a century leap year.

# year = int(input("Enter a year: "))

# if year % 100 == 0 and year % 400 == 0:
#     print("It is a Century Leap Year")

# else:
#     print("It is not a Century Leap Year")



# Q23 Determine the season based on the month number.

# month = int(input("Enter month number: "))

# if month==3 or month== 4 or month== 5:
#     print("Summer Season")

# elif month==6 or month== 7 or month== 8 or month==9:
#     print("Monsoon Season")

# elif month==10 or month== 11:
#     print("Autumn Season")

# elif month==12 or month== 1 or month== 2:
#     print("Winter Season")

# else:
#     print("Invalid Month Number")



# Q24 Find the number of days in a month.

# month = input("Enter your month:").lower()

# match month:

#     case "january":
#         print("31 days")

#     case "february":
#         print("28 days")

#     case "march":
#         print("31 days")

#     case "april":
#         print("30 days")

#     case "may":
#         print("31 days")

#     case "june":
#         print("30 days")

#     case "july":
#         print("31 days")

#     case "august":
#         print("31 days")

#     case "september":
#         print("30 days")

#     case "october":
#         print("31 days")

#     case "november":
#         print("30 days")

#     case "december":
#         print("31 days")

#     case _:
#         print("Invalid month")


# Q25 Check whether a password meets minimum conditions (length, digits, etc.).

# password = input("Enter password: ")

# if len(password) < 8:
#     print("Password is too short")

# elif password.isdigit():
#     print("Password must contain letters")

# else:
#     print("Valid Password")



# Q26 Determine ticket price based on age category.

# Age	Ticket Price
# Below 5 years	-> Free
# 5–12 years ->	₹50
# 13–59 years -> ₹100
# 60 years and above ->	₹70

# age = int(input("Enter your age: "))

# if age < 0:
#     print("Invalid age")

# elif age < 5:
#     print("Ticket is Free")

# elif age <= 12:
#     print("Ticket price: Rs. 50")

# elif age <= 59:
#     print("Ticket price: Rs. 100")

# else:
#     print("Ticket price: Rs. 70")



# Q27 Calculate discount based on purchase amount.

# Purchase Amount	Discount
# Below ₹1,000	-> 0%
# ₹1,000 – ₹4,999 -> 5%
# ₹5,000 – ₹9,999 -> 10%
# ₹10,000 and above	-> 20%

# amount = int(input("Enter amount: "))

# if amount <= 1000:
#     bill = (amount) * 0/100

# elif amount <= 4999:
#     bill = (amount) * 5/100

# elif amount <= 9999:
#     bill = (amount) * 10/100

# elif amount > 10000:
#     bill = (amount)  * 20/100

# print("Total disount:Rs.",bill)



# Q28 Check if a person is eligible for a driving license (age and eyesight condition).


# age = int(input("Enter your age: "))
# eyesight = input("Is your eyesight normal: ")

# if age >= 18 and eyesight == "yes":
#     print("Eligible for driving license")

# else:
#     print("Not eligible for driving license")



# Q29 Create a login system with username and password validation.

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "12345":
#     print("Login Successful")

# elif username != "admin":
#     print("Invalid Username")

# else:
#     print("Invalid Password")

# Q30 Create a menu-driven program using if-elif-else with options like:
# Addition
# Subtraction
# Multiplication
# Division
# Exit

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# print("5. Exit")

# choice = int(input("Enter your choice: "))

# if choice == 1:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Addition =", a + b)

# elif choice == 2:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Subtraction =", a - b)

# elif choice == 3:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Multiplication =", a * b)

# elif choice == 4:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     if b == 0:
#         print("Cannot divide by zero")
#     else:
#         print("Division =", a / b)

# elif choice == 5:
#     print("Thank you! Exiting...")

# else:
#     print("Invalid choice")