

a = [1,2]
print ("hello")

try:
    print (b)
except Exception as exception:
    print (exception)
    print ("some thing wrong above")
else:
    print (a)
    print ("No Error above")   # when your try block fails
finally:
    print ("always will get excuted")   # clean up


print ("world")

c = {"a":1}
a = [1,2]

try:
    print (c['b'])
except KeyError as err:
    print (err,type(err))
    print ("return mail to customer c complaining about the formula variable b")
    c["b"] = 3 

try:
    print (a[2])
except IndexError as err:
    print (err,type(err))
    print ("return mail to customer a complaining about the list length")
    a.append(1)



print ("hello world")
print (c)

try:
    print (c['a'])
    print (a[2])
except Exception as err:
    print (err,type(err))
    print ("return mail to customer c complaining about the formula variable b")
    c["b"] = 3 
    print ("return mail to customer a complaining about the list length")
    a.append(1)

print (a)
print (a[2])

dict_var = {"a":[0.5],"b":[1,1],"c":"1"}
try:

    d = ((dict_var["a"][0] / dict_var["b"][1]) + dict_var["b"][0] + int(dict_var["c"]))
    print (d)
    if (d >= 3):
        raise Exception("own exception")

except NameError as err:
    print ("in the name error exception - ")
    print ("MAIL TO CUSTOMER COMPLAINING ABOUT THE VARIABLE")
    print (err,type(err))
except KeyError as err:
    print ("in the key error exception - ")
    print ("MAIL TO CUSTOMER COMPLAINING ABOUT MISSING DICTIONARY KEY")
    print (err,type(err))
except IndexError as err:
    print ("in the index error exception - ")
    print ("MAIL TO CUSTOMER COMPLAINING ABOUT LIST IS NOT POPULATED")
    print (err,type(err))
except ZeroDivisionError as err:
    print ("in the ZERO error exception - ")
    print ("MAIL TO CUSTOMER COMPLAINING ABOUT A ZERO DENOMINATOR VALUE IN THE GIVEN DICT")
    print (err,type(err))
except TypeError as err:
    print ("in the Type error exception - ")
    print ("MAIL TO CUSTOMER COMPLAINING ABOUT INVALID DATA TYPE")
    print (err,type(err))
except ValueError as err:
    print ("in the Value error exception - ")
    print ("MAIL TO CUSTOMER COMPLAINING ABOUT INVALID VALUE")
    print (err,type(err))
except Exception as err:
    print ("MAIL TO CUSTOMER COMPLAINING ABOUT THE EXCEEDING VALUE")
    print ("in the base exception")
    print (err, type(err))
else:
    print ("NO ERRORS")
    print ("UPDATING THE DB")
finally:
    print ("MAIL TO BOSS - SENT MAIL TO CUSTOMER ABOUT THE STATUS")



