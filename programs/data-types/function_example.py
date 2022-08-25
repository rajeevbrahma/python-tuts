

a = 1
b = 2

def add():
    global a,b
    a = a+b
    b = a+b
    return (a,b,a+b)

print ("a - ",a,"b - ",b)
print (add())
print ("a - ",a,"b - ",b)



