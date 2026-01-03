'''
# 1] wap to print  1 -3 
i = 1
while i<=3:
    print(i,end=" ")
    i+= 1
'''

# 2] wap to print 3 - 1
'''
i = 3
while i>=0:
    print(i,end=" ")
    i-=1
# 3 2 1 0 
'''
'''
# 3] wap to print 0 - 20 even numbers

i = 0
while i <= 20:
    print(i,end=" ")
    i += 1

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
'''

# 4] wap to print 1 - 10 odd numbers
'''
i = 1
while i <= 10:
    print(i,end=" ")
    i += 1

# 1 2 3 4 5 6 7 8 9 10 
'''

'''
# 5] wap to print 1 - 10 even numbers

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
# 2 4 6 8 10 
'''

# 06] wap to print 2 to 10 odd numbers
'''
i = 2
i+= 1
while i <= 10:
    if i %2 == 1:
        print(i, end=" ")
    i += 2
# 3 5 7 9 
'''
'''
i = 2
i+= 1
while i <= 10:
    print(i,end=" ")
    i += 2

# 3 5 7 9
'''
'''
# 7] wap to print A - Z

i = ord('A')
while i <= ord('Z'):
    print(chr(i), end=" ")
    i += 1

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
'''
'''
# 8] wap to print a-z vowels

i = ord('a')

while i <= 122 :
    if chr(i) in 'aeiou':
        print(chr(i), end=" ")
    i += 1
# a e i o u 

'''

'''
# 9] wap to print A - Z consonants

i = ord('A')
while i <= 90:
    if chr(i) not in 'AEIOU':
        print(chr(i),end=" ")
    i += 1

# B C D F G H J K L M N P Q R S T V W X Y Z
'''
'''
# 10] wap to print square if the number is even, cube if the number is odd from 1 - 5

i = 1
while i <= 5:
    if i %2 == 0:
        print(i**2 , end= ' ')
    else:
        print(i**3, end=" ")
    i += 1

# 1 4 27 16 125 
'''
