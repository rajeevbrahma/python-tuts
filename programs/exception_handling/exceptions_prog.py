"""
    Error 

        SyntaxError

    Exceptions

        ZeroDivisionError
        NameError
        TypeError


"""




try:
    a = 1/0
except ZeroDivisionError:
    print ("Zero Division Error")

try:
    a = 1/0
except Exception as e:
    print (e)

try:
    print (hello)
except NameError as e:
    print (e)
    print ("Name error")

try:
    'hello' + 2
except TypeError as e:
    print (e)
    print ("Type Error")

try:
    x = int(input("Enter a number"))
except ValueError as e:
    print (e)
    print ("Value Error")


try:
    import module
except ImportError as e:
    print (e)

list_var = [1,2]
try:
    list_var[3]
except IndexError as e:
    print (e)

dict_var = {"a":1,"b":2}
try:
    dict_var["c"]
except KeyError as e:
    print (e)




