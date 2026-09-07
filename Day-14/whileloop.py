'''
i = 1
while i<=10:
    print(i)
    i+=1

i=10
while i>0:
    print(i)
    i-=1

#even using while
i=2
while i<=100:
    print(i, end=' ')
    i+=2
    
#iterating a string
s=' python programming'

i=len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1

#removing the zero's in list
l=[1,2,34,0,0,0,8,5,6,33,0,35,9,7]
while 0 in l:
    l.remove(0)
print(l)


d={}
total_bill=0
while True:
    product =input("Enter name(for exit):")
    if product == 'exit':
        break
    price=int(input("Enter price:"))
    total_bill += price
    d[product] = price
print(d)
print("Total bill:", total_bill)
'''
i=0
while i<=10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print("Ennd of the loop")

#1-7   2-8,9,11,14,17,18,20























