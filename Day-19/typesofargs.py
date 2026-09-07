'''
#postional args - based on position of variables we can assign values
def display(name, email, password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display('xyz','xyz@gmail.com','xyz@123')
display('xyz@123','xyz@gmail.com','xyz')
display('xyz@gmail.com','xyz@123','xyz')


#Keyword args - depends on keywords
def display(name, email, password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display(name='xyz',email='xyz@gmail.com',password='xyz@123')
display(password='xyz@123',email='xyz@gmail.com',name='xyz')
display(email='xyz@gmail.com',password='xyz@123',name='xyz')


#Default args - if user not pass a value it take default value, it is in end of the arguments,we have to set default value to the parameter
def display(name='', email='@gmail.com', password=''):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display('xyz','xyz@gmail.com','xyz@123')
display('xyz','xyz@gmail.com')
display('xyz')


#variable length args - tuple format *single asset
#1-positional
def display(*names):
    print(names)

display('sajid')
display('sajid','abdul')
display('sajid','abdul','sai')
display('sajid','abdul','sai','vikas')
'''
#2-**multiple assets display ouptut as dictionary format
def display(**products):
    print(products)

display(bag=5000)
display(bag=5000, book=30)
display(bag=5000, book=30, bottle=300)















































































