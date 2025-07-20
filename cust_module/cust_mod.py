



"""
def decinalToBinary(n):
    '''Func. to convert Decial to Binary'''
    binary_digit=[]

    # Getting the binary digit
    while n>0:
        rem=n%2
        binary_digit.append(str(rem))
        n=n//2

    # Reversing the digit
    print("".join(reversed(binary_digit)))
    print(type(binary_digit))



def halfDiamond(n):
    '''Func. to print half dianond pattern !'''
    for i in range(1,n+1):
        # spaces
        for space in range(0,n-i):
            print(" ",end="")
    
        # Stars
        for start in range(0,2*i-1):
            print("*",end="")
        print()




print("Jai Bhole ki !")
print("Har Har MahaDev")
print("Jai Bhairava baba !!")

def greetings(name):
    return "Hello ! "+ name 

    

def patternNumber(n):
    '''Func. for pattern printing problems.'''

    val=1
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(val, end=" ")
            val+=1
        print(" ")

"""     

