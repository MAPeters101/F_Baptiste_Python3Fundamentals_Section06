"""
Question 1
Given this string of comma separated characters, create three new variables containing the unicode codepoint (in hex), uppercase and lower case versions of each character (also comma delimited).

For example, if the string was 'a, b, c' you should generate three lists that look like:

['0x61', '0x62', '0x63']
['a', 'b', 'c']
['A', 'B', 'C']
[You should use the split() and strip() functions, amongst others, to help you solve this.]

s = 'Π, ύ, θ, ω, ν'
Solution
First we'll split this string on the comma to get a list of the individual characters:

chars = s.split(',')
chars
Note that some of these strings have an extra space, so we'll need to strip it. Instead of creating a new list with the stripped characters, we'll just re-use the same chars list, replacing elements in the list:

chars[0] = chars[0].strip()
chars[1] = chars[1].strip()
chars[2] = chars[2].strip()
chars[3] = chars[3].strip()
chars[4] = chars[4].strip()

chars
Let's look at the first letter:

chars[0]
To find the unicode codepoint, we use the ord() function:

ord(chars[0])
To find the hex of that unicode code point, we use the hex() function:

hex(ord(chars[0]))
To find the upper case version, we use the upper() method:

chars[0].upper()
And to find the lower case version we use the lower() method:

chars[0].lower()
Next, let's create a list will all the code points:

code_points = [
    hex(ord(chars[0])),
    hex(ord(chars[1])),
    hex(ord(chars[2])),
    hex(ord(chars[3])),
    hex(ord(chars[4]))
]
code_points
Then the lower case versions:

lower = [
    chars[0].lower(), chars[1].lower(), chars[2].lower(), chars[3].lower(), chars[4].lower()
]
lower
And finally the uppercase versions:

upper = [
    chars[0].upper(), chars[1].upper(), chars[2].upper(), chars[3].upper(), chars[4].upper()
]
upper
Question 2
Using two types of string interpolation, and given the variable a that contains an integer, print out the following string for a:

The number ...value of a... is (or is not) even

For example, if a is 42, the your code should print:

'The number 42 is even'

But if a is 31, then the same code should print:

'The number 31 is not even'

Solution
Basically we want to interpolate the value of a in our string, and then interpolate either is or is not depending on whether the number is even or not.

To determine if a number is even, we can use the % operator and see if that is equal to 0:

4 % 2
5 % 2
To choose is or is not, we can use a ternary expression:

a = 42
'is' if a % 2 == 0 else 'is not'
a = 31
'is' if a % 2 == 0 else 'is not'
'is not'
Now we can create our string, using the format method first:

a = 31
'The number {} {} even'.format(a, 'is' if a % 2 == 0 else 'is not')
'The number 31 is not even'
And the exact same code works for any value of a:

a = 42
'The number {} {} even'.format(a, 'is' if a % 2 == 0 else 'is not')
'The number 42 is even'
Next, we can do the same thing using f-strings:

a = 31
f"The number {a} {'is' if a % 2 == 0 else 'is not'} even"
'The number 31 is not even'
And again, the exact same code works for any value of a:

a = -42
f"The number {a} {'is' if a % 2 == 0 else 'is not'} even"
'The number -42 is even'
Question 3
You are given two variables a and b (with b non-zero), and you need to generate a string that reads something like this:

'a / b = (result)'
But you want your string to be nicely formatted for display purposes, so you want to limit displaying possible digits after the decimal point in all your values to 4 digits.

Solution
a = 3.141592653589793
b = 6
We can use an f-string interpolation to create our string:

f'{a} / {b} = {a / b}'
'3.141592653589793 / 6 = 0.5235987755982988'
We're almost there - our display includes too many digits to be very readable, so we want to limit to 4 digits after the decimal point.

To do this, we'll use some formatting commands:

f'{a:.4f} / {b:.4f} = {a / b:.4f}'
'3.1416 / 6.0000 = 0.5236'
Alternatively we could have used the format() method:

'{:.4f} / {:.4f} = {:.4f}'.format(a, b, a / b)
'3.1416 / 6.0000 = 0.5236'
"""