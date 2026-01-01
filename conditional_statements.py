#1 wap to check the number is evenor not
'''
n = int(input("Enter the number : "))

if n % 2 == 0:
    print("Even number")
else:
    print("Not a even number")

# Enter the number : 52
# Even number

'''

# 2] wap to check the word is palindrome or not
'''
s = input("Enter the word : ")

if s[::-1] == s:
    print("palindrome")
else:
    print("not a palindrome")

# Enter the word : wow
# palindrome

'''

# 3]wap to check the number is even or not if even add it to a dict and value should be 1
#  else add it to a tuple
'''
n = int(input("Enter the number : "))
d = {}
t = tuple()
if n % 2 == 0:
    d[n] = 1
    print(d)
else:
    t += (n,)
    print(t)

# Enter the number : 25
# (25,)
# Enter the number : 4
# {4: 1}
'''

# 4] wap to check the string is even len or not
# if even get the first and last char
# else get the middle char
'''
s = input("Enter the string : ")

if len(s) % 2 == 0:
    print(f"the first char is {s[0]} and last char is {s[-1]}")
else:
    print(f"the middle chat is {s[len(s)//2]}")

# Enter the string : sohail
# the first char is s and last char is l

# Enter the string : sohai
# the middle chat is h

'''
# 5]wap to check the char is vowel or not 
# if vowel add it to a list
# else add it to a dict as key and value as not a vowel
'''
s = input("Enter the character : ")
l = []
d = {}
if s in "AEIOUaeiou":
    l.append(s)
    print(l)
else:
    d[s] = "not a vowel"
    print(d)

# Enter the character : z
# {'z': 'not a vowel'}
# Enter the character : e
# ['e']
'''

# 6]wap to check the character is upper case or not if yes convert it to lowercase
# else add it to the set
'''
s = input("Enter the character : ")
se = set()
if "A" <= s <= "Z":
    print(f"The lower case character is : {chr(ord(s)+32)}")
else:
    se.add(s)
    print(se)

# Enter the character : A
# The lower case character is : a
# Enter the character : u
# {'u'}
'''

# 7]wap to check the number is +ve and even or not
# if yes get the last digit
# else convert and add it to a new string
'''
n = int(input("Enter the number : "))
s = ""
if n>0 and n%2==0:
    print(f"the last digit is {n%10}")
else:
    s = str(n)
    print(s ,type(s))

# Enter the number : 28
# the last digit is 8
# Enter the number : 25
# 25 <class 'str'>
'''
# elif

# 8] wap to check the number is +ve or -ve or neutral
'''
n = int(input("Enter the number : "))

if n > 0:
    print(f"the number is positive {n}")
elif n < 0:
    print(f"the number is negative {n}")
else:
    print(f"the number is neutral {n}")

# Enter the number : 25
# the number is positive 25
# Enter the number : 0
# the number is neutral 0
# Enter the number : -25
# the number is negative -25
'''

# 9]wap to check the char is upper case / lower case / ascii digit/ spcl char
'''
s = input("Enter the char : ")

if 'A' <= s <= 'Z':
    print("The char is upper case")
elif 'a' <= s <= 'z':
    print("The char is lower case")
elif '0' <= s <= '9':
    print("The char is ascii digit")
else:
    print("The char is special character")

# Enter the char : r
# The char is lower case
# Enter the char : 5
# The char is ascii digit
# Enter the char : *
# The char is special character
# Enter the char : E
# The char is upper case
'''

# 10]wap to check the char is upper case / lower case / ascii digit/ spcl char
# if UP -> LC
# if LC -> UC
# if num -> get the square
# if spcl k -> previous and next
'''
s = input("Enter the char : ")

if 'A' <= s <= 'Z':
    print(chr(ord(s)+32))
elif 'a' <= s <= 'z':
    print(chr(ord(s)-32))
elif '0' <= s <= '9':
    print(int(s)**2)
else:
    print(f"previous char is {chr(ord(s)-1)} and next char is {chr(ord(s)+1)}")

# Enter the char : 5
# 25
# Enter the char : u
# U
# Enter the char : Y
# y
# Enter the char : @
# previous char is ? and next char is A
# Enter the char : _
# previous char is ^ and next char is `
'''

#  Nested if

# 11] wap to find the second greatest number from 3 numbers
'''
n1 = int(input("Enter the n1 number : ")) 
n2 = int(input("Enter the n2 number : ")) 
n3 = int(input("Enter the n3 number : ")) 

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f"{n2} is the second greatest number")
    elif n3 > n2:
        print(f"{n3} is the second greatest number")
    else:
        print("Enter the different numbres")
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f"{n1} is the second greatest number")
    elif n3 > n1:
        print(f"{n3} is the second greatest number")
    else:
        print("Enter the different numbres")
elif n3 > n1 and n3 > n2:
    if n1 > n2:
        print(f"{n1} is the second greatest number")
    elif n2 > n1:
        print(f"{n2} is the second greatest number")
    else:
        print("Enter the different numbres")
else:
    print("Enter the different numbres")

# Enter the n1 number : 50
# Enter the n2 number : 85
# Enter the n3 number : 20
# 50 is the second greatest number
'''

# 12] wap to check the char is upper case/ lower case/ ascii digit/ spcl char
# if upper case check vowel or not
# if lower case check consonant or not
# if digit check even or odd
# if spcl char repeat it for 5 times
'''
s = input("Enter the char : ")

if 'A' <= s <= 'Z':
    if s in 'AEIOU':
        print(f"{s} is upper case and a vowel")
    else:
        print(f"{s} is upper case but not a vowel")
        
elif 'a' <= s <= 'z':
    if s not in 'aeiou':
        print(f"{s} is small case and a consonent")
    else:
        print(f"{s} is small case but not a consonent")

elif '0' <= s <= '9':
    if int(s) % 2 == 0:
        print(f"{s} is even")
    else:
        print(f"{s} is odd")
else:
    print("it is a spcl char",s * 5,sep=",")

# Enter the char : 8
# 8 is even
# Enter the char : i
# i is small case but not a consonent
# Enter the char : r
# r is small case and a consonent
# Enter the char : E
# E is upper case and a vowel
# Enter the char : @
# it is a spcl char,@@@@@
'''


# 13] check whether a string is empty or not
# check wheather a number lies within a given range --- > 1 - 30
# check if a person is eligible to vote (age >= 18)
'''
# str is empty or not
s = input("Enter the string : ")

if s == '':
    print("string is empty")
else:
    print("string is not empty")

# Enter the string : sohail
# string is not empty
# Enter the string : 
# string is empty
'''

'''
# n lies b/w range 

n = int(input("Enter the number : "))

if n > 0 and n < 30:
    print(f"{n} lies between 1 and 30")
else:
    print(f"{n} does not lies between 1 and 30")

# Enter the number : 25
# 25 lies between 1 and 30
# Enter the number : 55
# 55 does not lies between 1 and 30
'''

'''
# eligible to vote or not
n = int(input("Enter the number : "))

if n >= 18:
    print("youre eligible for vote")
else:
    print("youre not eligible for vote")

# Enter the number : 25
# youre eligible for vote
# Enter the number : 16
# youre not eligible for vote
'''

# match case

# 14] match case to select the language
'''
select = int(input("Enter a number : "))

match select:
    case 1 :
        print("you have selected telugu language.")
    case 2 :
        print("you have selected english language.")
    case 3:
        print("you have selected kannada language.")
    case 4 :
        print("you have selected hindi language.")
    case _ :
        print("select proper number.")

# Enter a number : 3
# you have selected kannada language.
# Enter a number : 8
# select proper number.
# Enter a number : 4
# you have selected hindi language.
'''
# 15] match case to select the day in a week
'''
select = int(input("Enter a number : "))

match select:
    case 1 :
        print("you have selected a sunday.")
    case 2 :
        print("you have selected a monday.")
    case 3:
        print("you have selected a tuesday.")
    case 4 :
        print("you have selected a wednesday.")
    case 5 :
        print("you have selected a thursday.")
    case 6 :
        print("you have selected a friday.")
    case 7 :
        print("you have selected a saturday.")
    case _ :
        print("select proper number.")

# Enter a number : 5
# you have selected a thursday.
# Enter a number : 2
# you have selected a monday.
# Enter a number : 8
# select proper number
'''