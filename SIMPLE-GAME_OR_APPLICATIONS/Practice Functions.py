##Bansari Shah
##ICS3U0
##Practices - Functions
##08 Nov 2020

##Question_1
def demo(name, age):
    print(name, age)
demo("Ben", 25)

##Question_2
## accept a variable length of  argument and print all arguments value
def func1(*args):
    for i in args:
        print(i)
func1(20,30,10,50)

##Question_3
def outerFun(a, b):
    square = (a**2)
    def innerFun(a, b):
        return (a+b)
    add = innerFun(a, b)
    return (add+5)

print(outerFun(5,10))

##Question_4

