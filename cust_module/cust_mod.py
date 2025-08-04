

"""

def array2d(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end=" ")
        print()



def linearSearch(array, key):

    n = len(array)

    for i in range(n):
        if array[i] == key:
            return i
            
    return -1

if __name__ == "__main__":
    idx = linearSearch(array, key)
    if idx == -1:
        print("Key is not present in the given array")
    else:
        print(idx)

    


def mountain(array):
    ans = 0
    i = 1
    while i < len(array) -1:
        isPrime = array[i] > array[i-1] and array[i] > array[i+1]
        if isPrime:
            cnt = 1
            j = i
            # Move backwards
            while j > 0 and array[j-1] < array[j]:
                cnt += 1
                j -= 1

            # Move forward
            j = i
            while j < len(array) -1 and array[j] > array[j + 1]:
                cnt += 1
                j += 1
            
            # breath of peak
            ans = max(cnt, ans)
            i = j

        else:
            i += 1
    
    return ans





arry = [10, 5, 2, 3, -6, 9, 11]
s = 4

def pariSumHashing(array, s):
    htable = {}

    for i in arry:
        y = s - i
        if(y in htable):
            return [i, y]
        else: htable[i] = True
    return []



string = "pratulbhatt"


def firstrepeatchar(string):

    table = {}
    for  char in string.lower():
        if char in table:
            return char
        elif char != " ":
            table[char] = True
    return


def isPrime(n):

    for i in range(2,n):
        if n%i == 0:
            return False
        
    return True

    if(isPrime(n)):
            print("Yes number is prime")
    else:
        print("Number is not prime")

    for i in range(1,n+1):
        if(isPrime(i)):
            print(i,end=",")



def decimalToBinaryBitwise(n):
    '''Using bitwise'''
    binary_digit=[]

    # Getting the binary digit
    while n>0:
        last_bit = n & 1
        binary_digit.append(str(last_bit))
        n=n>>1

    # Reversing the digit
    print("".join(reversed(binary_digit)))




def decimalToBinary(n):
    '''Func. to convert Decimal to Binary'''
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

