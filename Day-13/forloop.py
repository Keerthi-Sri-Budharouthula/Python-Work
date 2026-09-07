'''s = "Python Programming"
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])
        


l=[23,45,12,34,50,24,35,68,75,34,10]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
        print(i,l[i])
print(sum)

#factorial program
n=int(input("Enter the number:"))
fact = 1
for i in range(1, n+1):
    fact *=i
print(f"Factorial of {n} is {fact}")

#print student marks details
data={}
n = int(input("Enter the no of students:"))
max_marks=0
for i in range (n):
    name=input("Enter the name:")
    marks=int(input("Enter the marks:"))
    if marks > max_marks:
        max_marks=marks
    data[name]=marks
print(data)
print("Maximum marks:",max_marks)
'''
products={}
n = int(input("Enter no of products:"))
total_bill=0
for i in range(1,1+n):
    product=input(f"product-{i}:")
    quantity=int(input(f"quantity-{i}:"))
    price=int(input(f"price-{i}:"))
    
    final_bill=price*quantity
    total_bill += final_bill
    products[product]= f'{price} * {quantity} = {final_bill}'
print(products)
print("Total Bill:",total_bill)
