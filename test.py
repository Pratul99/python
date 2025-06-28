 # integer, float, boolean, reassign

age = 7
height = 0.9
male = true
age = 8



sum = 4 + 2   # 6
diff =  4 - 2   # 2
div = 4 / 2  # 2
mult = 4 * 2  # 8
expo = 3 ** 8   # 
floor = 10 // 3  # 3
mog = 17 % 15 # 2


# round function

ex_var = 1.23 + 2.80
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

number1 = 12
number2 = "5.3251"
number_total = number1 + float(number2)
print(number_total)
# output : 17.3251
print(type(number_total))
# output : float