# Q1 Even or Odd Function
# Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".

# def is_even(num):

#     if num%2==0:

#         return "Even"

#     else:

#         return "Odd"

# print(is_even(3))



# Q2 Largest of Two Numbers
# Write a function largest(a, b) that returns the larger number.

# def largest(a,b):

#     if a>b:

#         return "a is greater"

#     else:

#         return "b is greater"

# print(largest(5,9))



# Q3 Print Numbers
# Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

# def print_numbers(n):

#     for i in range(1,n):

#         print(i)

# print_numbers(11)



# Q4 Sum of Numbers
# Write a function sum_n(n) that returns the sum of numbers from 1 to n.

# def sum_n(n):

#     total=0

#     for i in range (1,n):

#         total=total+i

#     return total

# print(sum_n(5))



# Q5 Multiplication Table
# Write a function table(n) that prints the multiplication table of n from 1 to 10.

# def table(n):

#     for i in range(1,11):

#         print(f"{i} x {n} = {i * n}")

# table(4)



# Q6 Count Even Numbers 
# Write a function that takes a list and returns how many even numbers it contains.
# Example:
# count_even([1, 2, 3, 4, 6])
# Output:3 

# numbers = [1,2,3,4,5,6,7,8]

# def count_even(numbers):

#     count = 0

#     for num in numbers:

#         if num % 2 == 0:

#             count += 1

#     return count

# print(count_even(numbers))           



# Q7 Find Maximum
# Without using max(), write a function that returns the largest number in a list.

# numbers = [12,55,11,33,22,44]

# def largest_number(numbers):
#     largest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             largest = num

#     return largest

# print(largest_number(numbers))



# Q11 FizzBuzz
# Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".

# def fizzbuzz():
#     for i in range(1, 21):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# fizzbuzz()



# Q12 Palindrome Checker
# Write a function that returns True if a string is a palindrome.

# def palindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False

# print(palindrome("madam"))



# Q13 Count Vowels
# Write a function that counts the vowels in a string.

# def count_vowels(s):
#     count = 0

#     for char in s:
#         if char.lower() in "aeiou":
#             count += 1

#     return count

# print(count_vowels("Hello World"))



# Q14 Second Largest Number
# Write a function that returns the second largest number in a list without using sort().

# numbers = [10, 20, 5, 40, 30]

# def second_largest(numbers):
#     largest = numbers[0]
#     second = None

#     for num in numbers:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num != largest and (second is None or num > second):
#             second = num

#     return second


# print(second_largest(numbers))



# Q15 Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.

# def guessing_game():
#     number = 7

#     guess = 0

#     while guess != number:
#         guess = int(input("Guess a number between 1 and 10: "))

#         if guess == number:
#             print("Correct! You win!")
#         else:
#             print("Wrong! Try again.")

# guessing_game()



#       Write a function grade(marks) that:
# Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"

# def grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     elif marks >= 60:
#         return "D"
#     else:
#         return "F"


# print(grade(95))
# print(grade(85))
# print(grade(75))
# print(grade(65))
# print(grade(50))