"""

        Arithmetic operators
                                +, -, *, **, /, %, //
        Assignment operators
                                =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
        Comparison operators
                                ==, != , > , < , >=, <=
        Logical operators
                                and, or, not        
        Identity operators
                                is, is not
        Membership operators
                                in, not in


"""

# Arithmetic operators

from re import A


print (1+2)
print (2-1)
print (3*4)
print (3**4)
print (3/4)
print (3%4)
print (3//4)

# Assignment operators

assignee = 10
print (assignee)

assignee += 10   # => assignee = assignee + 10
print (assignee)
assignee -= 10   # => assignee = assignee - 10
print (assignee)
assignee *= 10   # => assignee = assignee * 10
print (assignee)
assignee **= 10   # => assignee = assignee ** 10
print (assignee)
assignee /= 10   # => assignee = assignee / 10
print (assignee)
assignee %= 10   # => assignee = assignee % 10
print (assignee)
assignee //= 10   # => assignee = assignee // 10
print (assignee)
# assignee = 0.0
# assignee &= 10.0   # => assignee = assignee & 10
# print (assignee)
# assignee |= 10   # => assignee = assignee | 10
# print (assignee)
# assignee ^= 10   # => assignee = assignee ^ 10
# print (assignee)
# assignee <<= 10   # => assignee = assignee << 10
# print (assignee)
# assignee >>= 10   # => assignee = assignee >> 10
# print (assignee)

# Comparision operator

print (1==2)
print (1!=2)
print (1>2)
print (1<=2)
print (1>=2)

# Exercise - Comparison operator on Strings


# Logical Operators
print (1 and 2)
print (1 or 2)
print (not 1)

"""
        And Truth Table
        1 and 1 1
        0 and 1 0     
        1 and 0 
        0 and 0

        Or Truth Table
        1 or 1
        0 or 1
        1 or 0
        0 or 0

Exercise - try these combinations with both "and" and "or"

        a = "hai", b = "hello"
        a = "",    b = "hello"
        a = "hai", b = "hello"
        a = "",    b = ""

"""


# Exercise - Logical Operators on Strings



print (1 is 2)          # wont accept
print (1 is not 2)      # wont accept

name_1 = "Python"
name_2 = "python"

print (name_1 is name_2)
print (name_1 is not name_2)

name_1 = "pyt"
name_2 = "python"
print (name_1 in name_2)
print (name_1 not in name_2)
