#iterate a sequence datatypes - str,list, tuple, set, dict range()
'''
for var in seq:
    print(var)

#str
s= 'Codegnan'
for ch in s:
    if ch in 'aeiouAEIOU':
        print(ch)

#list
l = [10,23,30,45,1,3,15,16,18,19,21]
for i in l:
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"Odd")

#tuple
marks=(90,20,35,46,78,92,87,48)
for mark in marks:
    if mark>35:
        print(mark, "pass")
    else:
        print(mark, "fail")

#set
followers ={'srinu','sajid','dheeraj','sathvik','karthik'}
for i in followers:
    print(i)

#dict
bus={'s1':'booked','s2':'Available','s3':'Available','s4':'booked','s5':'Available',}
for seat in bus:
    if bus.get(seat)=='Available':
        print(seat,bus.get(seat))
        
#range(start,end+1,step) a sequence to generate a numeric numbers
for i in range(1,11):
    print(i)

for i in range(2,51,2):
    print(i,end=" ")

for i in range(1,50,2):
    print(i,end=" ")

for i in range(1,100,2):
    print(i,end=" ")

for i in range(5,51,5):
    print(i)
'''
n= int(input("Enter the tanle no: "))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')