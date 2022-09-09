
def add(a,b):
    return (a+b)
    # print (a+b)

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


 #  y = (9)-3  - equation 1 
 # y = (42/7)-3+6
 # y = (4*3*2)+(4/2)-1

def equations():
    a = 5
    b = 4
    c = 3
    result = add(a,b)
    print ("line 22",result)
    print (add(a,b),c)
    print (sub(add(a,b),c))

    # y = (42/7)-3+6

    print (add(sub(div(42,7),3),6))

    print (sub(add(mul(mul(4,3),2),div(4,2)),1))


    # sub(result,c)


equations()
   

