# 1. Data Types
# Q1 Find the data type of every value in a mixed list.

# my_list = [10, "Hello", 3.5, True, 20, "Python"]

# for i in my_list:
#     print(i, type(i))


# Q2 Convert a nested list into a tuple of tuples.

# my_list = [[1, 2], [3, 4], [5, 6]]

# result = ()

# for i in my_list:
#     result = result + (tuple(i),)

# print(result)


# Q3 Remove all duplicate values from a mixed list while preserving the original order.

# my_list = [10, 20, "Hello", 10, 30, "Hello"]

# new_list = []

# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)

# print(new_list)



# 2. Operators
# Q4 Check whether a number is a power of 2 using operators.

# num = 16

# if num > 0 and (num & (num - 1)) == 0:
#     print("Power of 2")
# else:
#     print("Not a power of 2")


# Q5 Swap two numbers using bitwise XOR.


# Q6 Find whether a number is divisible by both 4 and 6 using logical operators.

# num = 24

# if num % 4 == 0 and num % 6 == 0:
#     print("Divisible by both")
# else:
#     print("Not divisible by both")


# Q7 Calculate the total electricity bill using different unit rates.

# units = int(input("Enter electricity units: "))

# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = (100 * 2) + (units - 100) * 3
# else:
#     bill = (100 * 2) + (100 * 3) + (units - 200) * 5

# print("Total bill:", bill)



# 3. Conditional Statements
# Q8 Check whether three sides can form a triangle.

# a = 5
# b = 6
# c = 7

# if a + b > c and a + c > b and b + c > a:
#     print("Valid triangle")
# else:
#     print("Not a valid triangle")


# Q9 Determine the type of triangle (Equilateral, Isosceles, Scalene).

# a = 5
# b = 5
# c = 5

# if a + b > c and a + c > b and b + c > a:
#     if a == b and b == c:
#         print("Equilateral")
#     elif a == b or b == c or a == c:
#         print("Isosceles")
#     else:
#         print("Scalene")
# else:
#     print("Invalid triangle")


# Q10 Create a simple ATM menu (Withdraw, Deposit, Balance).

# balance = 5000

# print("1. Withdraw")
# print("2. Deposit")
# print("3. Balance")

# choice = int(input("Enter your choice: "))

# if choice == 1:
#     amount = int(input("Enter amount: "))
#     if amount <= balance and amount > 0:
#         balance = balance - amount
#         print("Withdraw successful")
#     else:
#         print("Insufficient balance")

# elif choice == 2:
#     amount = int(input("Enter amount: "))
#     if amount > 0:
#         balance = balance + amount
#         print("Deposit successful")
#     else:
#         print("Invalid amount")

# elif choice == 3:
#     print("Balance:", balance)

# else:
#     print("Invalid choice")


# Q11 Calculate income tax based on different tax slabs.
# Assume:
# Income up to ₹2,50,000 = No tax
# ₹2,50,001 to ₹5,00,000 = 5%
# ₹5,00,001 to ₹10,00,000 = 20%
# Above ₹10,00,000 = 30%

# income = int(input("Enter your income: "))

# if income <= 250000:
#     tax = 0
# elif income <= 500000:
#     tax = income * 0.05
# elif income <= 1000000:
#     tax = income * 0.20
# else:
#     tax = income * 0.30

# print("Income tax:", tax)


# Q12 Create a menu-driven calculator using if-elif.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter choice: "))

# if choice == 1:
#     print(a + b)
# elif choice == 2:
#     print(a - b)
# elif choice == 3:
#     print(a * b)
# elif choice == 4:
#     if b != 0:
#         print(a / b)
#     else:
#         print("Cannot divide by zero")
# else:
#     print("Invalid choice")



# 4. Loops
# Q13 Print all prime numbers between 1 and n.

# n = int(input("Enter n: "))

# for num in range(2, n + 1):
#     count = 0

#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1

#     if count == 2:
#         print(num)


# Q14 Find the factorial of a number using a loop.

# num = int(input("Enter a number: "))

# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial:", fact)


# Q15 Print the Fibonacci series up to n terms.

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c


# Q16 Check whether a number is an Armstrong number.

# num = int(input("Enter a number: "))

# temp = num
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total = total + digit ** 3
#     temp = temp // 10

# if total == num:
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")


# Q17 Reverse a number and check if it is a palindrome.

# num = int(input("Enter a number: "))

# temp = num
# reverse = 0

# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp = int(temp / 10)

# print("Reverse:", reverse)

# if num == reverse:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# Q18 Find the Greatest Common Divisor (GCD) of two numbers.

# a = 12
# b = 18

# while b != 0:
#     c = b
#     b = a % b
#     a = c

# print("GCD:", a)



# 5. Functions
# Q19 Write a function to check if a string is a palindrome.

# def palindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False

# print(palindrome("madam"))


# Q20 Write a function to count vowels and consonants in a string.

# def count_letters(s):
#     vowels = 0
#     consonants = 0

#     for i in s:
#         if i.isalpha():
#             if i.lower() in "aeiou":
#                 vowels += 1
#             else:
#                 consonants += 1

#     print("Vowels:", vowels)
#     print("Consonants:", consonants)

# count_letters("Hello World")


# Q21 Create a function to calculate simple and compound interest.

# def interest(p, r, t):
#     si = (p * r * t) / 100
#     ci = p * (1 + r / 100) ** t - p

#     print("Simple Interest:", si)
#     print("Compound Interest:", ci)

# interest(1000, 5, 2)


# Q22 Write a function to return all factors of a number.

# def factors(num):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             print(i)

# factors(12)


# Q23 Write a function to find the second-largest number in a list.

# def second_largest(numbers):
#     largest = numbers[0]
#     second = None

#     for i in numbers:
#         if i > largest:
#             second = largest
#             largest = i
#         elif i != largest:
#             if second is None or i > second:
#                 second = i

#     return second

# print(second_largest([10, 20, 30, 40, 50]))



# 6. Lists 
# Q24 Merge two lists without duplicates.

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# c = list(set(a + b))

# print(c)


# Q25 Find the second-largest and second-smallest elements.

# numbers = [10, 20, 30, 40, 50]

# smallest = numbers[0]
# second_smallest = None

# largest = numbers[0]
# second_largest = None

# for i in numbers:
#     if i < smallest:
#         second_smallest = smallest
#         smallest = i
#     elif i != smallest:
#         if second_smallest is None or i < second_smallest:
#             second_smallest = i

#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i != largest:
#         if second_largest is None or i > second_largest:
#             second_largest = i

# print("Second smallest:", second_smallest)
# print("Second largest:", second_largest)


# Q26 Rotate a list to the left by k positions.

# numbers = [1, 2, 3, 4, 5]

# k = 2

# result = numbers[k:] + numbers[:k]

# print(result)


# Q27 Separate even and odd numbers into two lists.

# numbers = [1, 2, 3, 4, 5, 6]

# even = []
# odd = []

# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even:", even)
# print("Odd:", odd)


# Q28 Find the common elements between two lists.

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# common = []

# for i in a:
#     if i in b and i not in common:
#         common.append(i)

# print(common)



# 7. Tuples & Sets
# Q29 Count the frequency of each element in a tuple.

# t = (1, 2, 2, 3, 3, 3)

# for i in t:
#     count = t.count(i)
#     print(i, "=", count)


# Q30 Find the union, intersection, and difference of two sets.


# Q31 Check whether one set is a subset of another.

# a = {1, 2}
# b = {1, 2, 3, 4}

# if a.issubset(b):
#     print("A is subset of B")
# else:
#     print("A is not subset of B")


# 8. Dictionaries
# Q32 Count the frequency of words in a sentence.

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# d = {}

# for i in words:
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d)


#  Q33 Create a dictionary from two lists (keys and values).

# keys = ["name", "age", "city"]
# values = ["Rahul", 20, "Pune"]

# d = {}

# for i in range(len(keys)):
#     d[keys[i]] = values[i]

# print(d)


# Q34 Sort a dictionary by its values.

# d = {"a": 30, "b": 10, "c": 20}

# result = {}

# values = list(d.values())
# values.sort()

# for v in values:
#     for k in d:
#         if d[k] == v:
#             result[k] = v

# print(result)



# 9. File Handling
# Q35 Read a text file and count the number of lines, words, and characters.

# file = open("data.txt", "r")

# text = file.read()

# lines = text.splitlines()
# words = text.split()
# characters = len(text)

# print("Lines:", len(lines))
# print("Words:", len(words))
# print("Characters:", characters)

# file.close()


# Q36 Copy only the even-numbered lines from one file to another.

# file = open("data.txt", "r")
# new_file = open("even.txt", "w")

# lines = file.readlines()

# for i in range(len(lines)):
#     if (i + 1) % 2 == 0:
#         new_file.write(lines[i])

# file.close()
# new_file.close()

# print("Even lines copied successfully")



# 10. Exception Handling
# Q37 Handle invalid integer input using try-except.

# try:
#     num = int(input("Enter a number: "))
#     print("Number:", num)

# except ValueError:
#     print("Please enter a valid integer")


# Q38 Handle file-not-found errors while reading a file.

# try:
#     file = open("data.txt", "r")

#     print(file.read())

#     file.close()

# except FileNotFoundError:
#     print("File not found")



# 11. Modules
# Q39 Create a random password generator using the random and string modules.


# Q40 Use the datetime module to calculate the number of days between two dates.

# date1 = 5
# date2 = 25

# difference = date2 - date1

# print("Total days:", difference)