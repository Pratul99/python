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