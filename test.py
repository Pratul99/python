 # integer, float, boolean, reassign

age = 7
height = 0.9
male = "true"
age = 8



sum = 4 + 2   # 6
diff =  4 - 2   # 2
div = 4 / 2  # 2
mult = 4 * 2  # 8
expo = 3 ** 8   # 
floor = 10 // 3  # 3
mod = 17 % 15 # 2


# round function

ex_var = 1.23 + 9,.22322
2.80
print(round(ex_var, 2))

#ex. 

pasta = 16.68  # penne 16 oz, pack of 12
sauce = 6.98  # Arrabiata sauce 24oz
garlic = 16.78  # 20 pack garlic clove
seasoning = 15.26  # Italian Seasoning
bread = 3.00  # Baguette twin pack
meatballs = 4.39  # 12 oz bag of meatballs
 
# numbers after the decimal will always have 2 numbers after its decimal point.
subtotal = round((pasta + sauce + garlic + seasoning + bread + meatballs), 2)
print(subtotal)


# ******************************** To get a perticular character using index number ********************************

ex_1 = "pratul"
print(ex_1[4])
or
print("apple"[3])


# ********************************  slicing string ********************************

ex_2 = "apricots"

print(ex_2[:3])     # apr    (start at 0 index num : one more then the index num you want i.e r,2)
print(ex_2[2:5])    # ric    (start at 2 index num : one more then the index num you want i.e c,4)
print(ex_2[4:])     # cots   (start at 4 index num : one more then the index num you want i.e last s,7)



# ********************************  concatenation ********************************

print("Har" + "Har" + "Mahadev")   # Har Har Mahadev
or
concatenated = "R2" + "-" + "D2"
print(concatenated) # R2-D2
print(concatenated[3]) # D
print(concatenated[1:4]) # 2-D


# ----------------------------------------------- xx -----------------------------------------------

# 24-05-2025 

# Single line comment use (#)
# Multi - line comments use (''' Comment inside ''')

# Python keyword to define a function
''' 
| Part          | Meaning                             |
| ------------- | ----------------------------------- |
| `def`         | Python keyword to define a function |
| `my_function` | Name of the function                |
| `()`          | Place for parameters (if needed)    |
| `:`           | Start of function body              |

'''

def my_function():
    ''' This is an example of function that gives multi-line comments

        My name is PRBB
    '''

print(my_function.__doc__)



# ----------------------------------------------- xx -----------------------------------------------

# 28-05-2025 

# Video 6a - What are Data Types (1)

text1 = "I am a string because I contain alphabets like A to Z"
text2 = "I am a string because I contain alphabets like a to z"
text3 = "I am a string because I contain numbers like 0 to 9"
text4 = "I am a string because I contain special characters like @#$%-*"
this_string_has_empty_values = ""
this_is_an_empty_string = ''

greetings = "Hello World"
print(greetings)
# output : Hello World

greetings = 'Hello World'
print(greetings)
# output : Hello World

multi_line_text = '''This is line 1 of the string variable named multi_line_text
This is line 2 of the string variable named multi_line_text
This is line 3 of the string variable named multi_line_text
This is line 4 of the string variable named multi_line_text
This is line 5 of the string variable named multi_line_text'''

text = "Single 'quotation marks' are allowed here but double \"quotation marks\" must be escaped here"
text = 'Single \'quotation marks\' must be escaped here but double "quotation marks" are allowed here'

text = "Your path name is c:\\users\\Mary"
print(text)
# output : Your path name is c:\users\Mary



# Video 6b - What are Data Types (1)

text = "Your path name is c:\users\Mary"
print(text)
# output : ERROR


# Video 6c - What are Data Types (1)
#raw string

text = r"Your path name is c:\users\Mary"
print(text)
# output : Your path name is c:\users\Mary

'''

In Python:
| Value                                 | `bool(value)` result |
| ------------------------------------- | -------------------- |
| `0`                                   | `False`              |
| Any non-zero number (e.g., `1`, `-3`) | `True`               |
| `''` (empty string)                   | `False`              |
| `'abc'` (non-empty string)            | `True`               |
| `[]`, `{}`, `None`                    | `False`              |
| Any non-empty list/dict/object        | `True`               |

'''

# Video 7 - What are Data Types (2)

num1 = 0
bool1 = bool(num1)
print(bool1)
# output : False

num1 = 6
bool1 = bool(num1)
print(bool1)
# output : True

num1 = -3.56
bool1 = bool(num1)
print(bool1)
# output : True

text1 = "0"
bool1 = bool(text1)
print(bool1)
# output : True

text1 = ""
bool1 = bool(text1)
print(bool1)
# output : False

i_am_None = None
print(i_am_None)
# output : None

i_am_None = None
print(type(i_am_None))
# output : NoneType

i_am_None = None
print(bool(i_am_None))
# output : False


# Video 8 - String Manipulation & Typecasting (1)


print("Hi" * 3)
# output : HiHiHi

print("*" * 10)
# output : **********

text1 = "I am"
text2 = "here"
print(text1 + " " + text2)
# output : I am here

text1 = "I am"
text2 = "here"
print(text1, text2)
# output : I am here

#  Formatted string literal, also known as an f-string. A string prefixed with f allows you to insert variables or expressions inside {} placeholders.

print(f'Hello World')
# output : Hello World

text1 = "I am"
text2 = "here"
print(f'Hi, {text1} {text2}')
# output : Hi, I am here

# Hello Jack
# 0123456789
text = "Hello Jack"
print(text[0])
# output : H

# Hello Jack
# 0123456789
text = "Hello Jack"
print(text[4])
# output : o

#   H  e  l  l  o     J  a  c  k
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
text = "Hello Jack"
print(text[-1])
# output : k

#   H  e  l  l  o     J  a  c  k
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
text = "Hello Jack"
print(text[-9])
# output : e

# Hello Jack
# 0123456789
text = "Hello Jack"
print(text[:5])
# output : Hello

#   H  e  l  l  o     J  a  c  k
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
text = "Hello Jack"
print(text[-3:])
# output : ack

# When determining the last character to be included in the slicing it is ALWAYS the ending Index position -  1.
# Note that starting index is inclusive and ending index is exclusive.

# Hello Jack
# 0123456789
text = "Hello Jack"
print(text[6:10])
# output : Jack

#   H  e  l  l  o     J  a  c  k
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
text = "Hello Jack"
print(text[-9:-6])
# output : ell

# Hello Jack
# 0123456789
text = "Hello Jack"
print(text[4:])
# output : o Jack

#   H  e  l  l  o     J  a  c  k
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
text = "Hello Jack"
print(text[-4:])
# output : Jack


# Video 9 - String Manipulation & Typecasting (2)

text = "Please convert me to all uppercase"
print(text.upper())
# output : PLEASE CONVERT ME TO ALL UPPERCASE
print(text)
# output : Please convert me to all uppercase
text_new = text.upper()
print(text_new)
# output : PLEASE CONVERT ME TO ALL UPPERCASE

text = "Please convert me to all lowercase"
print(text.lower())
# output : please convert me to all lowercase

text = "Count number of u's in me"
print(text.count("u"))
# output : 3

text = "Replace this with that"
print(text.replace("this", "that"))
# output : Replace that with that

text = "What is the length of this text"
print(len(text))
# output : 31

text = "   Strip both ends   "
print(text.strip())
# output : Strip both ends
print(len(text.strip()))
# output : 15

text = "   Strip left end   "
print(text.lstrip())
# output : Strip left end

text = "   Strip right end   "
print(text.rstrip())
# output :    Strip right end

text = "abcdEf"
print(text.isalnum())
# output : True
print(text.isalpha())
# output : True
print(text.isdigit())
# output : False
print(text.isupper())
# output : False
print(text.islower())
# output : False

text = "12345"
print(text.isalnum())
# output : True
print(text.isalpha())
# output : False
print(text.isdigit())
# output : True
print(text.isupper())
# output : False
print(text.islower())
# output : False

text = "abc def"
print(text.isalnum())
# output : False
print(text.isalpha())
# output : False


# Video 10a - String Manipulation & Typecasting (3)

number = 5.3251
number_int = int(number)
print(number_int)
# output : 5
print(type(number_int))
# output : int

text = "5"
text_int = int(text)
print(text_int)
# output : 5
print(type(text_int))
# output : int

number = 1
number_float = float(number)
print(number_float)
# output : 1.0
print(type(number_float))
# output : float

text = "5.3251"
text_float = float(text)
print(text_float)
# output : 5.3251
print(type(text_float))
# output : float

number = 1
number_str = str(number)
print(number_str)
# output : 1
print(type(number_str))
# output : str

number = 5.3251
number_str = str(number)
print(number_str)
# output : 5.3251
print(type(number_str))
# output : str

number1 = 12
number2 = 5.3251
number_total = number1 + number2
print(number_total)
# output : 17.3251
print(type(number_total))
# output : float

number1 = 12
number2 = "5.3251"
number_total = number1 + number2
print(number_total)
# output : ERROR

# int + float = float

number1 = 12
number2 = "5.3251"
number_total = number1 + float(number2)
print(number_total)
# output : 17.3251
print(type(number_total))
# output : float


# Video 10b - String Manipulation & Typecasting (3)

number1 = 12
number2 = "5.3251"
number_total = number1 + number2
# output : ERROR


# Video 10c - String Manipulation & Typecasting (3)

# int + float = float
number1 = 12
number2 = "5.3251"
number_total = number1 + float(number2)
print(number_total)
# output : 17.3251
print(type(number_total))
# output : float


# ----------------------------------------------- xx -----------------------------------------------

# 29-05-2025 

# Video 11 - What are Data Structures (1)

'''
| Category | Types Included                     |
| -------- | ---------------------------------- |
| Numeric  | `int`, `float`, `complex`          |
| Text     | `str`                              |
| Boolean  | `bool`                             |
| Sequence | `list`, `tuple`, `range`           |
| Set      | `set`, `frozenset`                 |
| Mapping  | `dict`                             |
| Binary   | `bytes`, `bytearray`, `memoryview` |
| Special  | `NoneType`                         |


| Data Type | Allows Duplicates?           | Notes                                  |
| --------- | ---------------------------- | -------------------------------------- |
| list      | ✅ Yes                        | Maintains order, mutable and allows repeats     |
| tuple     | ✅ Yes                        | Maintains order, Immutable but allows duplicates        |
| str       | ✅ Yes                        | Each character can repeat              |
| bytes     | ✅ Yes                        | Duplicate byte values allowed          |
| bytearray | ✅ Yes                        | Like bytes but mutable                 |
| range     | ✅ Technically Yes            | Values generated are unique by default |
| dict      | ✅ Values: Yes 🚫 Keys: No | Duplicate keys are not allowed         |
| set       | 🚫 No                        |  Unordered, mutable, Only unique elements                   |
| frozenset | 🚫 No                        | unordered, Immutable set with unique elements     |


🧠 Core Data Types in Python
1. Numeric Types
Data Type	Example	        Description
int	        10, -5	        Integer numbers
float	    3.14, -0.001	Floating-point (decimal) numbers
complex	    2 + 3j	        Complex numbers with real and imaginary parts

2. Text Type
Data Type	Example	                Description
str	        'Hello', "World"	    String (text) data, enclosed in quotes

3. Boolean Type
Data Type	Example     	Description
bool	    True, False     Logical values used in conditions

4. Sequence Types
Data Type	Example	    Description
list	    [1, 2, 3]	Ordered, mutable collection
tuple	    (1, 2, 3)	Ordered, immutable collection
range	    range(5)	Sequence of numbers, often used in loops

5. Set Types
Data Type	Example	                    Description
set	        {1, 2, 3}	                Unordered collection of unique items
frozenset	frozenset([1, 2, 3])	    Immutable set (can't be changed)

6. Mapping Type
Data Type	Example	                            Description
dict	    {'name': 'Alice', 'age': 25}    	Key-value pairs (unordered, mutable)

7. Binary Types
Data Type	    Example	                        Description
bytes	        b'Hello'	                    Immutable sequence of bytes
bytearray	    bytearray(b'Hello')	            Mutable sequence of bytes
memoryview	    memoryview(b'Hello')	        Memory-efficient view of bytes or bytearrays

8. None Type
Data Type	    Example	        Description
NoneType	    None	        Represents no value or null

🧪 Type Checking & Conversion
To check a data type: type(x)

To convert between types:

int('5') → 5

str(100) → '100'

list('abc') → ['a', 'b', 'c']

'''

# item   apples oranges mangoes pears
# index     0      1       2      3
this_is_a_fruits_list = ["apples", "oranges", "mangoes", "pears"]
print(this_is_a_fruits_list)
# output : ["apples", "oranges", "mangoes", "pears"]
print(this_is_a_fruits_list[0])
# output : apples
print(this_is_a_fruits_list[1])
# output : oranges
print(this_is_a_fruits_list[2])
# output : mangoes
print(this_is_a_fruits_list[3])
# output : pears



# The len() function returns the number of elements in a list, not the index range.
#len() counts how many items exist (total quantity)

this_is_a_fruits_list[2] = "grapes"
print(this_is_a_fruits_list[2])
# output : grapes
print(this_is_a_fruits_list)
# output : ["apples", "oranges", "grapes", "pears"]
print(len(this_is_a_fruits_list))
# output : 4




# item   apples oranges grapes pears
# index     0      1       2     3      left to right
# index    -4     -3      -2    -1      right to left
this_is_a_fruits_list = ["apples", "oranges", "grapes", "pears"]
print(this_is_a_fruits_list[-1])
# output : pears
print(this_is_a_fruits_list[-2])
# output : grapes
print(this_is_a_fruits_list[-3])
# output : oranges
print(this_is_a_fruits_list[-4])
# output : apples

# item   apples 5 True 1.2 house
# index     0   1   2   3    4
list1 = ["apples", 5, True, 1.2, "house"]
print(type(list1[0]))
# output : str
print(type(list1[1]))
# output : int
print(type(list1[2]))
# output : bool
print(type(list1[3]))
# output : float
print(type(list1[4]))
# output : str

list1.append(False)
print(list1)
# output : ["apples", 5, True, 1.2, "house", False]

list1.insert(3, "insert me at index 3")
print(list1)
# output : ["apples", 5, True, "insert me at index 3", 1.2, "house", False]

del list1[5]
print(list1)
# output : ["apples", 5, True, "insert me at index 3", 1.2, False]

text = "Split me into a list"
i_am_a_list = text.split()
print(i_am_a_list)
# output : ["Split", "me", "into", "a", "list"]
print(type(i_am_a_list))
# output : list

text = ""
i_am_a_list = ["Join ", "me ", "into ", "a ", "string"]
text = text.join(i_am_a_list)
print(text)
# output : Join me into a string
print(type(text))
# output : str



# Video 12 - What are Data Structures (2)

# item   apples oranges grapes pears
# index     0      1       2     3
this_is_a_1_dimensional_list = ["apples", "oranges", "grapes", "pears"]
print(this_is_a_1_dimensional_list[0])
# output : apples
print(this_is_a_1_dimensional_list[1])
# output : oranges
print(this_is_a_1_dimensional_list[2])
# output : grapes
print(this_is_a_1_dimensional_list[3])
# output : pears

# item       ["a", "b", "c", "d"], ["e", "f", "g", "h"], ["i", "j", "k", "l"]
# 1st index    0    0    0    0      1    1    1    1      2    2    2    2
# 2nd index    0    1    2    3      0    1    2    3      0    1    2    3
this_is_a_2_dimensional_list = [["a", "b", "c", "d"], ["e", "f", "g", "h"], ["i", "j", "k", "l"]]
print(this_is_a_2_dimensional_list[0][0])
# output : a
print(this_is_a_2_dimensional_list[0][1])
# output : b
print(this_is_a_2_dimensional_list[0][2])
# output : c
print(this_is_a_2_dimensional_list[0][3])
# output : d
print(this_is_a_2_dimensional_list[1][0])
# output : e
print(this_is_a_2_dimensional_list[1][1])
# output : f
print(this_is_a_2_dimensional_list[1][2])
# output : g
print(this_is_a_2_dimensional_list[1][3])
# output : h
print(this_is_a_2_dimensional_list[2][0])
# output : i
print(this_is_a_2_dimensional_list[2][1])
# output : j
print(this_is_a_2_dimensional_list[2][2])
# output : k
print(this_is_a_2_dimensional_list[2][3])
# output : l



# Video 13 - What are Data Structures (3)

dictionary_for_city_weather_pair = {"Singapore": 30, "Paris": 15, "Sydney": 19, "Tokyo": 15}
print(dictionary_for_city_weather_pair)
# output : {"Singapore": 30, "Paris": 15, "Sydney": 19, "Tokyo": 15}

dictionary_for_city_weather_pair["Shanghai"] = 13
print(dictionary_for_city_weather_pair)
# output : {"Singapore": 30, "Paris": 15, "Sydney": 19, "Tokyo": 15, "Shanghai": 13}

del dictionary_for_city_weather_pair["Singapore"]
print(dictionary_for_city_weather_pair)
# output : {"Paris": 15, "Sydney": 19, "Tokyo": 15, "Shanghai": 13}

dictionary_for_city_weather_pair["Sydney"] = 16
print(dictionary_for_city_weather_pair)
# output : {"Paris": 15, "Sydney": 16, "Tokyo": 15, "Shanghai": 13}

print(dictionary_for_city_weather_pair["Paris"])
# output : 15

dictionary_for_team_country_pair = {"Team C": "Japan", "Team J": "United Kingdom", "Team B": "Germany", "Team A": "Japan"}
print(dictionary_for_team_country_pair)
# output : {"Team C": "Japan", "Team J": "United Kingdom", "Team B": "Germany", "Team A": "Japan"}

dictionary_for_child_number_child_age_pair = {56: 7, 32: 7, 78: 8}
print(dictionary_for_child_number_child_age_pair)
# output : {56: 7, 32: 7, 78: 8}



# Video 14 - What are Data Structures (4)

this_is_a_fruits_set = {"apples", "oranges", "grapes", "pears"}
this_is_a_fruits_set.add("pineapples")
print(this_is_a_fruits_set)
# output : {"apples", "oranges", "grapes", "pears", "pinesapples"}

this_is_a_fruits_set.remove("grapes")
print(this_is_a_fruits_set)
# output : {"apples", "oranges", "pears", "pinesapples"}

this_is_a_fruits_set.remove("apples")
this_is_a_fruits_set.add("mangoes")
print(this_is_a_fruits_set)
# output : {"mangoes", "oranges", "pears", "pinesapples"}
this_is_a_fruits_set.add("mangoes")
print(this_is_a_fruits_set)
# output : {"mangoes", "oranges", "pears", "pinesapples"}


# Video 15 - What are Operators (1)
'''
| Category   | Operators                                       |                           |
| ---------- | ----------------------------------------------- | ------------------------- |
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**`             |                           |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=`                |                           |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` |                           |
| Logical    | `and`, `or`, `not`                              |                           |
| Bitwise    | `&`, \`                                         | `, `^`, `\~`, `<<`, `>>\` |
| Membership | `in`, `not in`                                  |                           |
| Identity   | `is`, `is not`                                  |                           |

| Operator | Name                | Purpose / Usage                            | Example  | Result |
| -------- | ------------------- | ------------------------------------------ | -------- | ------ |
| `/`      | Division            | Divides and returns a **float** result     | `7 / 2`  | `3.5`  |
| `//`     | Floor Division      | Divides and returns **floor (int)** result | `7 // 2` | `3`    |
| `%`      | Modulus (Remainder) | Returns **remainder** of division          | `7 % 2`  | `1`    |
| `==`     | Equal to            | Checks **if two values are equal**         | `7 == 7` | `True` |


1. Arithmetic Operators

| Operator | Description         | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 3`  | `8`    |
| `-`      | Subtraction         | `5 - 3`  | `2`    |
| `*`      | Multiplication      | `5 * 3`  | `15`   |
| `/`      | Division            | `5 / 2`  | `2.5`  |
| `//`     | Floor Division      | `5 // 2` | `2`    |
| `%`      | Modulus (remainder) | `5 % 2`  | `1`    |
| `**`     | Exponentiation      | `2 ** 3` | `8`    |

2. Comparison (Relational) Operators

| Operator | Description      | Example           |
| -------- | ---------------- | ----------------- |
| `==`     | Equal to         | `5 == 5` → `True` |
| `!=`     | Not equal to     | `5 != 3` → `True` |
| `>`      | Greater than     | `5 > 3` → `True`  |
| `<`      | Less than        | `5 < 3` → `False` |
| `>=`     | Greater or equal | `5 >= 5` → `True` |
| `<=`     | Less or equal    | `3 <= 5` → `True` |

3. Assignment Operators

| Operator | Description             | Example              |
| -------- | ----------------------- | -------------------- |
| `=`      | Assign                  | `x = 5`              |
| `+=`     | Add and assign          | `x += 2` (x = x + 2) |
| `-=`     | Subtract and assign     | `x -= 1`             |
| `*=`     | Multiply and assign     | `x *= 3`             |
| `/=`     | Divide and assign       | `x /= 2`             |
| `//=`    | Floor divide and assign | `x //= 2`            |
| `%=`     | Modulus and assign      | `x %= 2`             |
| `**=`    | Exponent and assign     | `x **= 2`            |

4. Logical Operators
| Operator | Description                  | Example            |
| -------- | ---------------------------- | ------------------ |
| `and`    | True if both are true        | `x > 2 and x < 10` |
| `or`     | True if at least one is true | `x < 2 or x > 5`   |
| `not`    | Reverses boolean value       | `not(x > 5)`       |

5. Bitwise Operators

| Operator | Description       | Example         |     |         |
| -------- | ----------------- | --------------- | --- | ------- |
| `&`      | AND               | `5 & 3` → `1`   |     |         |
| \`       | \`                | OR              | \`5 | 3`→`7\` |
| `^`      | XOR               | `5 ^ 3` → `6`   |     |         |
| `~`      | NOT (invert bits) | `~5` → `-6`     |     |         |
| `<<`     | Left shift        | `5 << 1` → `10` |     |         |
| `>>`     | Right shift       | `5 >> 1` → `2`  |     |         |

6. Membership Operators

| Operator | Description         | Example                     |
| -------- | ------------------- | --------------------------- |
| `in`     | True if present     | `'a' in 'cat'` → `True`     |
| `not in` | True if not present | `'z' not in 'cat'` → `True` |

7. Identity Operators

| Operator | Description          | Example      |
| -------- | -------------------- | ------------ |
| `is`     | Same object?         | `x is y`     |
| `is not` | Not the same object? | `x is not y` |



** Rules of Operator Precedence **

Operator                  Description
--------                  -----------
()                        parenthesis
**                        exponentiation
+x, -x                    unary plus, unary minus
*, /, //, %               multiplication, division, floor div, modulo
+, -                      addition, subtraction
==, !=, >, >=, <, <=,     comparisions, identity, membership
is, is not, in, not in
not                       logical not
and                       logical and
or                        logical or

'''

number1 = 19
number2 = 5
print(-number1)
# output : -19
print(number1 + number2)
# output : 24
print(number1 - number2)
# output : 14
print(number1 * number2)
# output : 95
print(number1 / number2)
# output : 3.8
print(number1 % number2)
# output : 4
print(number1 ** number2)
# output : 2476099
print(number1 // number2)
# output : 3
print(-number1 // number2)
# output : -4

number1 = 5

number2 = 5
number2 += 3
print(number2)
# output : 8

number3 = 5
number3 -= 3
print(number3)
# output : 2

number4 = 5
number4 *= 3
print(number4)
# output : 15

number5 = 5
number5 /= 2
print(number5)
# output : 2.5

number1, number2, text1 = 3, 7, "multiple assignment"
print(number1)
#output : 3
print(number2)
# output : 7
print(text1)
# output : multiple assignment

number1 = 9
number2 = 11
print(number1 > number2)
# output : False
print(number1 < number2)
# output : True
print(number1 == number2)
# output : False
print(number1 != number2)
# output : True
print(number1 >= number2)
# output : False
print(number1 <= number2)
# output : True

number1 = 9
number2 = 11
number3 = 7
number4 = 6
print(number1 > number2 and number3 > number4)
# output : False
print(number1 > number2 or number3 > number4)
# output : True
print(not number1 > number2)
# output : True


# Video 16 - What are Operators (2)

number1 = 10
print(type(number1) is int)
# output : True
print(type(number1) is not int)
# output : False

number2 = 10.2
print(type(number2) is float)
# output : True
print(type(number2) is int)
# output : False
print(type(number2) is not str)
# output : True

text1 = "Hello World"
text2 = "Hello"
text3 = "hello"

print(text2 in text1)
# output : True
print(text2 not in text1)
# output : False
print(text3 in text1)
# output : False

print(100/10*10)
# output : 100



# Video 17 - What are Conditionals (1)

'''
| Keyword              | Purpose                                      |
| -------------------- | -------------------------------------------- |
| `if`                 | Executes a block if condition is true        |
| `elif`               | Checks more conditions if previous are false |
| `else`               | Executes if all above conditions are false   |
| `and` / `or` / `not` | Combine or invert conditions                 |
| Ternary              | One-line `if-else`                           |

ex. Ternary
x = 10
result = "Positive" if x > 0 else "Non-positive"
print(result)

'''

your_score = 48
passing_score = 50
if your_score >= passing_score:
    print("Congrats!")
    print("You have passed!")
else:
    print("You did not pass.")
    print("Please try again next time.")
print("Thank you for taking the exam.")

# output : You did not pass.
# output : Please try again next time.
# output : Thank you for taking the exam.


# Video 18 - What are Conditionals (2)

your_score = 89
passing_score = 50
credit_score = 70
distinction_score = 90
if your_score >= distinction_score:
    print("Congrats!")
    print("You have passed with DISTINCTION!")
elif your_score >= credit_score:
    print("Congrats!")
    print("You have passed with CREDIT!")
elif your_score >= passing_score:
    print("Congrats!")
    print("You have passed!")
else:
    print("You did not pass.")
    print("Please try again next time.")
print("Thank you for taking the exam.")

# output : Congrats!
# output : You have passed with CREDIT!
# output : Thank you for taking the exam.


your_score = 89

passing_score = 50
credit_score = 70
distinction_score = 90

if your_score >= distinction_score:
    print("Congrats!")
    print("You have passed with DISTINCTION!")
elif your_score >= credit_score:
    print("Congrats!")
    print("You have passed with CREDIT!")
    if your_score >= distinction_score - 5:
       print("You are less than 5 points to scoring DISTINCTION!")
elif your_score >= passing_score:
    print("Congrats!")
    print("You have passed!")
else:
    print("You did not pass.")
    print("Please try again next time.")

print("Thank you for taking the exam.")

# output : Congrats!
# output : You have passed with CREDIT!
# output : You are less than 5 points to scoring DISTINCTION!
# output : Thank you for taking the exam.




# Video 19 - What are Loops (1)

'''
| Loop Type | When to Use                                   |
| --------- | --------------------------------------------- |
| `for`     | When iterating over a known sequence or range |
| `while`   | When looping based on a condition             |

| Statement  | Purpose                                |
| ---------- | -------------------------------------- |
| `break`    | Exit the loop immediately              |
| `continue` | Skip the rest of the loop and continue |
| `pass`     | Do nothing (placeholder)               |

'''

count = 1
while count <= 10:
    print(count)
    count = count + 1

# output : 1
# output : 2
# output : 3
# output : 4
# output : 5
# output : 6
# output : 7
# output : 8
# output : 9
# output : 10


count = 1
while count <= 10:
    print(count)
    count = count + 1
    to_exit = input("Enter e if you wish to exit ")
    if to_exit == "e":
        break


count = 0
while count <= 9:
    count = count + 1
    if count%2:
        continue
    print(count)

# output : 2
# output : 4
# output : 6
# output : 8
# output : 10

# Video 20 - What are Loops (2)

for count in range(10):
    print(count+1)

# output : 1
# output : 2
# output : 3
# output : 4
# output : 5
# output : 6
# output : 7
# output : 8
# output : 9
# output : 10


for count in range(2, 15):
    print(count)

# output : 2
# output : 3
# output : 4
# output : 5
# output : 6
# output : 7
# output : 8
# output : 9
# output : 10
# output : 11
# output : 12
# output : 13
# output : 14


for count in range(2, 14, 4):
    print(count)

# output : 2
# output : 6
# output : 10


for count in range(20, 7, -5):
    print(count)

# output : 20
# output : 15
# output : 10


for count_a in range(1, 4):
    for count_b in range(1, 4):
        for count_c in range(1, 4):
            print(count_a, count_b, count_c)

# output : 1 1 1
# output : 1 1 2
# output : 1 1 3
# output : 1 2 1
# output : 1 2 2
# output : 1 2 3
# output : 1 3 1
# output : 1 3 2
# output : 1 3 3
# output : 2 1 1
# output : 2 1 2
# output : 2 1 3
# output : 2 2 1
# output : 2 2 2
# output : 2 2 3
# output : 2 3 1
# output : 2 3 2
# output : 2 3 3
# output : 3 1 1
# output : 3 1 2
# output : 3 1 3
# output : 3 2 1
# output : 3 2 2
# output : 3 2 3
# output : 3 3 1
# output : 3 3 2
# output : 3 3 3


student_list = ["Mary", "John", "Mike", "Alice"]
for student_name in student_list:
    print(student_name)

# output : Mary
# output : John
# output : Mike
# output : Alice


student_list = ["Mary", "John", "Mike", "Alice"]
index = 0
while index < len(student_list):
    print(student_list[index])
    index += 1

# output : Mary
# output : John
# output : Mike
# output : Alice
# ----------------------------------------------- xx -----------------------------------------------

# 0-0-2025 

