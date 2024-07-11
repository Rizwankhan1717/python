x = 99 

def f1():
    # x = 88
    def f2():
        print(x)
    f2()
f1()

# note : if x is given inside the funtion ,it takes 88 as x ,
#        if not, then its takes global variable, which is 99 