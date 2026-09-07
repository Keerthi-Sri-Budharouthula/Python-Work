'''
def display(n):
    n=n+10 #Local variable
    print("Inside:",n)

n=10  #global variable
display(n)
print("outside:",n)

#global variable
def display():
    print("Inside:",n)

n=10  #global variable
display()
print("outside:",n)

#local variable -it generates error
def display():
    n=10  #local variable
    print("Inside:",n)

display()
print("outside:",n)


#if declare global variable inside function we didn't  want to pass the parameters
def display():
    global n
    n =n+10
    print("Inside:",n)

n=10
display()
print("Outside:",n)

def display():
    #global n
    n='PFS'
    print("Updated Course:",n)

n='JFS'
display()
print("Final Course:",n)

def display():
    n='JFS'
    def update():
        nonlocal n #inside the funstion we use it/only effect the parent function 
        n='PFS'
        print("Updated Course:", n)
    update()
    print("Final Corse:",n)

display()
'''
l=[1,2,3,4,5]
max=20
sum=10
print(sum)











































































