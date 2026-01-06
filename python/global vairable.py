#method 1
print("METHOD 1:- ")
x=3

def myfunc():
    print(3 + x)

myfunc() #calling function
print("")

#============================================================================
#method 2 
print("METHOD 2:-")
x=3 

def myfunc2():
    x=4 #LOCAL VARIABLE
    print("inside function:",6*x)
myfunc2() #function calling

#outside function
print("outside function",x)

#======================================================
#METHOD 3:-

def myfunc3():
    global x
    x = 12
    print(x)

print(myfunc3())
