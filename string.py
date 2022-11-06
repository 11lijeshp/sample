'''b='asd dfa sfdf '
a=b[0:2]+b[-8:-1]
a='\000\145\154\154\177'
print(a)
a="".join(reversed('dfggf'))
print(a)'''
from ctypes.wintypes import HGDIOBJ
from operator import xor
from platform import freedesktop_os_release
'''y=23567.50698979
print('number is: {:13.2f}'.format(y))
a='freedeskto'
b='HGDggfhjIOBJ'
print(repr(a and b))
print(repr(a or b))
print(repr(b or a))
print(repr(b and a))'''
'''# python program to demonstrate the use of
# max() function

# maximum alphabetical character in
# "geeks"
string = "geeks"
print(max(string))

# maximum alphabetical character in
# "raj"
string = "raj"
print(max(string))'''
'''text = 'geeks for geeggks'

# Splits at space
print(text.rsplit())

word = 'geeks, for, geeksgfgf'

# Splits at ','
print(word.split(','))

word = 'geeks:for:geeks'

# Splitting at ':'
print(word.split(':'))

word = 'CatBatSatFatOr'

# Splitting at t
print(word.rsplit('t'))

word = 'geeks, for, geeks, pawan'

# maxsplit: 0
print(word.split(', ', 0))

# maxsplit: 4
print(word.split(', ', 4))

# maxsplit: 1
print(word.rsplit(', ', 1))'''
'''
# Python 3 Program to show working
# of translate() method

# First String
firstString = "gef"

# Second String
secondString = "eks"

# Third String
thirdString = "ge"

# Original String
string = "geeks"
print("Original string:", string)

translation = string.maketrans(firstString,secondString,thirdString)
print(translation)
# Translated String
print("Translated string:",
	string.translate(translation))'''
''''''
# Program to count
# the number of each
# vowel in a string

# string of vowels
v = 'aeiou'

# change this value for a different result
str = 'Hello, have you try geeksforgeeks?'

# input from the user
# str = input("Enter a string: ")

# caseless comparison
str = str.casefold()

# make a dictionary with
# each vowel a key and value 0
c = {}.fromkeys(v,0)
print(c)

# count the vowels
for char in str:
		if char in c:
				c[char] += 1
print(c) '''
