for index in range(1, 101):
    if index % 5 == 0 and index % 3 == 0:
        print("FizzBuzz")
    elif index % 3 == 0:
            print("Fizz")
    elif index % 5 == 0:
            print("Buzz")
    else:
        print(index)


# Challenge #1

new_list = []

def capital_indexes(string):
    for index, letter in enumerate(string):
        if index.isupper():
            new_list.append(letter)

    return new_list

capital_indexes("TEsT")

# Challenge #2
from math import ceil
def mid(string):
    str_length = len(string)
    if str_length % 2 == 0:
        return ""
    else:
        mid_str = int(str_length / 2)
        # print(mid_str)
        return string[mid_str]

mid("abc")

# Challenge #3
def online_count(dic):
    count = 0
    for index, value in dic.items():
        if value == "online":
            count += 1
    return count

online_count({
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
})


# Challenge 4
import random
def random_number():
    return random.randint(0, 101)

def only_ints(param1, param2):
    if type(param1) == int and type(param2) == int:
        # print("is int")
        return True
    else:
        # print("is not int")
        return False

#
(only_ints(1, 2))

# Challenge 5

def double_letters(word):
    letter1 = ""
    my_list = []
    for index in range(len(word)):
        letter1 = word[index - 1]
        if letter1 == word[index]:
            my_list.append(True)
        else:
            my_list.append(False)
    if True in my_list:
        return True
    else:
        return False
double_letters('hello')

# Challenge 6

def add_dots(string):
    new_string = ""
    for letter in string:
        new_string += letter
        new_string += "."
    return new_string[:-1]

# def remove_dots(string):
#     new_letter = ""
#     for letter in string:
#         if letter != ".":
#             new_letter += letter
#     return new_letter

def remove_dots(s):
    return s.replace(".", "")

remove_dots("asd.f")

# Challenge 7

def count(string):
    vowel_count = 0
    vowels = "aeiouy"
    for letter in string:
        if letter in vowels:
            vowel_count += 1

    if "ed" in string:
        vowel_count -= 1
    return vowel_count


count("terminator")

# Challenge 8
# Anagrams
# Two strings are anagrams if you can make one from the other by rearranging the letters.
# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.
# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.



# My solution was to create one of the strings to a list because strings in python are immutable
# then proceed create a loop to check each letter with the list if there was a match
# look for the char index and was deleted from the list
# at the end just check if the list is not empty


def is_anagram(string, string2):
    list_str = list(string2)
    for letter in string:
        if letter in list_str:
            i = list_str.index(letter)
            del(list_str[i])
    if len(list_str) == 0:
        return True
    else:
        return False


# easy solution
# There is this method that sorts the string then you can check if both strings are equal.
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)


is_anagram("Rodrigo", "Rodroigo")


# Challenge 9
# Flatten a list
#
# Write a function that takes a list of lists and flattens it into a one-dimensional list.
# Name your function flatten. It should take a single parameter and return a list.
# For example, calling:
# flatten([[1, 2], [3, 4]])
# Should return the list:
# [1, 2, 3, 4]


# My Solution:
# First I created a variable that is a list then proceed to do a for loop to check every item on the list
# Finally proceed to add that item to the variable that I created and to return that list once the loop is done.
def flatten(lists):
    final_list = []
    for list in lists:
        final_list += list
    return final_list

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [item for inner_list in outer_list for item in inner_list]

flatten([[1, 2], [3, 4]])


# Challenge
# Min-maxing
# Define a function named largest_difference that takes a list of numbers as its only parameter.
# Your function should compute and return the difference between the largest and smallest number in the list.
# For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
# You may assume that no numbers are smaller or larger than -100 and 100.


# My Solution I know of this two Functions that returns the minimum and maximum value max(), min()
def largest_difference(list):
    highest_number = max(list)
    lowest_number = min(list)
    return highest_number - lowest_number


# My Second Solution was to create 2 variables that was assign the first value from the list
# then proceed to create loops to find the highest and lowest value and assign those values to the variables
# finally return the difference of those 2 variables
def largest_difference(list):
    highest_number = lowest_number = list[0]
    for number in list:
        if number > highest_number:
            highest_number = number
    for number in list:
        if number < lowest_number:
            lowest_number = number

    return highest_number - lowest_number

largest_difference([1, 55, 2548, 3689410 , -25561 , -515869654])


# Challenge
# Divisible by 3
# Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.
# For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2 as a remainder.

# Solution check if remainder of number % 3 == 0.
def div_3(number):
    if number % 3 == 0:
        return True
    else:
        return False

# Or


def div_3(number):
    return number % 3 == 0


# Challenge
# Tic tac toe input
#
# Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:
#
# 1:  X | O | X
#    -----------
# 2:    |   |
#    -----------
# 3:  O |   |
#
#     A   B  C
#
# The board is represented as a 2D list:
#
# board = [
#     ["X", "O", "X"],
#     [" ", " ", " "],
#     ["O", " ", " "],
# ]
#
# Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].
#
# Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.
#
# For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.


# My Solution was to give to the variable column the correspondent value using a if statement
# and to the row value convert it to an int and return it as a tuple
def get_row_col(string):
    if "A" in string:
        column = 0
    elif "B" in string:
        column = 1
    else:
        column = 2
    row = int(string[1]) - 1
    return (row, column)

# This solution was after look and see its more easy to create a dict and give all the values for the column
def get_row_col(string):
    translate = {"A": 0, "B": 1, "C": 2}
    column = translate[string[0]]
    row = int(string[1]) - 1
    return (row, column)

get_row_col('B1')



# Challenge
# Palindrome
#
# A string is a palindrome when it is the same when read backwards.
#
# For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".
#
# Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.

# Solution it is possible give negative values to the index in strings my solution was to create a variable that was assign -1
# this will check the last index value from the same string and check it with the first value
# all of this with a for loop
def palindrome(string):
    i = -1
    for letter in string:
        if letter != string[i]:
            return False
        i -= 1
    return True


# Challenge
# Up and down
#
# Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.
#
# For example, calling up_down(5) should return (4, 6).

# Solution I mean I have no explanation its just common sense.
def up_down(number):
    return (number -1, number + 1)


# Challenge
# Consecutive zeros
#
# The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:
#
# "1001101000110"
#
# The biggest number of consecutive zeros is 3.
#
# Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.


# Solution First I created 3 variables, one to keep the amount of zeros using a for loop and inside this using if statement
# checking the current number with the next one if they were not the same the amount of zeros will be pass to the max_zeros
# if this one was lesser then the current store number then we proceed to reset the zeros variable back to 0
# last we have to catch an IndexError.
def consecutive_zeros(binary_string):
    max_zeros = zeros = 0
    i = 1
    for number in binary_string:
        if number == "0":
            zeros += 1
        try:
            if binary_string[i] != "0":
                if max_zeros <= zeros:
                    max_zeros = zeros
                zeros = 0
        except IndexError:
            if max_zeros <= zeros:
                max_zeros = zeros
        i += 1
    return max_zeros


consecutive_zeros("0")

# Challenge
# All equal
#
# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
#
# For example, calling all_equal([1, 1, 1]) should return True.


# Solution First created a variable and assign True bool then using a for loop compare the first item in the list with
# every other item if one of them don't match we assign a False bool to the variable break the loop and return the value
def all_equal(items):
    is_equal = True
    for item in items:
        if items[0] != item:
            is_equal = False
            break
    return is_equal


all_equal([])

# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden
# is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost
# always capitalizing every word. For simplicity, you'll have to capitalize each word,
# check out how contractions are expected to be in the example below.
#
# Your task is to convert strings to how they would be written by Jaden Smith.
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
#
# Example:
#
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"


# Solution I split the string using the split Function then proceed to do a for loop to get each item and to
# use the capitalize function to create a capital word then added to the string finally using the strip Function
# to cut any blank spaces at the beggining and end.

def to_jaden_case(string):
    string_list = string.split()
    new_string = ""
    for word in string_list:
        new_string += " " + word.capitalize()
    return new_string.strip()


# This was one of the answers the Join Function joins strings and you can use any char to join them in this case
# we use a blank space but you can use any char then uses list comprehension.
def toJadenCase(string):
    return "%".join(w.capitalize() for w in string.split())

# print(toJadenCase("Required. Any iterable object where all the returned values are strings"))


def number(bus_stops):
    persons = 0
    for stop in bus_stops:
        persons += stop[0] - stop[1]
    return persons

# List comprehension answer it is more short but it can be hard to understand for beginners
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
# Examples
#
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


# Solution for this I created two list comprehension then proceed to check which one has only 1 item in it
# then return the one that comes back True
def find_outlier(integers):
    odd = [number for number in integers if number % 2 != 0]
    even = [number for number in integers if number % 2 == 0]
    # for number in integers:
    #     if number % 2 != 0:
    #         odd.append(number)
    #     else:
    #         even.append(number)
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]


find_outlier([2, 4, 6, 8, 10, 3, 0])
find_outlier([160, 3, 1719, 19, 11, 13, -21])


# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.
#
# For example (Input --> Output):
#
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)


# Solution First I need it to know what the number was so I convert it to a string and add every char to a list then
# proceed to multiply every number in the list last proceed to give the new value to the number and add 1 to the counter
def persistence(n):
    count = 0
    while n > 9:
        result = 1
        num_list = []
        for char in str(n):
            num_list.append(char)
        for num in num_list:
            result *= int(num)
        n = result
        count += 1
    return count
