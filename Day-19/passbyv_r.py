#pass by value, pass by reference
#int float str list tuple set dict bool
#int float str tuple bool  effecting inside not outside-immutable(pass by value)
#list set dict effecting inside and outside also-mutable(pass by reference)
'''
def display(n):
    n = n+10
    print("Inside:",n)

n=10  
display(n)
print("outside:",n)


def display(n):
    n = 10.9
    print("Inside:",n)

n=10.5
display(n)
print("outside:",n)


def display(n):
    n = 'python'
    print("Inside:",n)

n='java'
display(n)
print("outside:",n)


def display(n):
    n = (1,2,3,4)
    print("Inside:",n)

n=(1,2,3)
display(n)
print("outside:",n)


def display(n):
    n = True
    print("Inside:",n)

n=False
display(n)
print("outside:",n)

def display(n):
    n.append(12)
    print("Inside:",n)

n=[1,2,3,4]
display(n)
print("outside:",n)

def display(n):
    n.add(12)
    print("Inside:",n)

n={1,2,3,4}
display(n)
print("outside:",n)
'''
def display(n):
    n[5]=6
    print("Inside:",n)

n={1:2,3:4}
display(n)
print("outside:",n)































































