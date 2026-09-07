Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
2**3
8
a%b
0
9%2
1
4**2
16


a=20
b=10
a>b
True
a<b
False
a>=b
True
a<=b
False
a==b
False
a!=b
True



c=10
c=c+10
c
20
c=c+20
c
40
c=c+40
c
80
c +=10
c
90
c-=50
c
40
c*=2
c
80
c**=2
c
6400
c%=3
c
1
c/=2
c
0.5
c//=1
c
0.0
c+=0.5
c
0.5


n=10
n%2==o
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    n%2==o
NameError: name 'o' is not defined
n%2==0
True
n%3==0
False
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n%8==0 or n%3==0
False
n<5
False
not n<5
True


#str list tuple set dict
s='codegnan'
'e' in s
True
'f' in s
False
'o' not in s
False
'f' not in s
True

l=[1,2,3,4,5]
5 in l
True
6in l
False
7 in l
False
2 in l
True
3 not in l
False

t=(1,2,3,4)
5 in t
False
4 in l
True
2 not in l
False
2 in l
True

s={1,4,9}
1 in s
True
4 not in t
False
9 in t
False
7 in t
False

d={'name':'abdul','batch':63,'course':'python}
   
SyntaxError: unterminated string literal (detected at line 1)
d={'name':'abdul','batch':63,'course':'python'}
   
'name' in d
   
True
'abdul' in d
   
False
63 not in d
   
True
63 in d
   
False


#identity operator is, is not
   
l=[1,2,3,4]
   
m=[1,2,3,4]
   
id(l)
   
2912247509696
id(m)
   
2912247571136
l is m
   
False
l is not m
   
True
n=l
   
id(n)
   
2912247509696
l is n
   
True
n is m
   
False
n is not m
   
True
n is not l
   
False


#immutable & mutable
   
str='codegnan'
   
id(str)
   
2912247540464
str='codegnan course'
   
id(str)
   
2912247611760

set={1,2,3}
   
id(set)
   
2912247128448
set.add(4)
   
s
   
{1, 4, 9}
set
   
{1, 2, 3, 4}
id(set)
   
2912247128448
#same id will generated in mutable data type set, list, dict
   

#based on 0's and 1's
   
9&10
   
8
9|10 #or
   
11
9^10#not
   
3
8>>3
   
1
8<<2
   
32
~8
   
-9
~12
   
-13
~45
   
-46

a= 10
   
b=10.3
   
c='codegnan'
   
print(a,b,c)
   
10 10.3 codegnan
print("a value is",a)
   
a value is 10
# coma(,) separation
   
print("a value is",a,"b value is",b,"c value is",c)
   
a value is 10 b value is 10.3 c value is codegnan
>>> print(a,b,c)
...    
10 10.3 codegnan
>>> print(a,b,c,sep='')
...    
1010.3codegnan
>>> print(a,b,c,sep='\t')
...    
10	10.3	codegnan
>>> print(a,b,c,sep='\t',end='@')
...    
10	10.3	codegnan@
>>> print(a,b,c,sep='\t',end='\n\n')
...    
10	10.3	codegnan

>>> print(f'a={a} b={b} c={c}')
...    
a=10 b=10.3 c=codegnan
>>> print('a=%d b=%f c=%s' %(a,b,c))
...    
a=10 b=10.300000 c=codegnan
>>> print(f'a={a} b={b} c={c}')#easy format
...    
a=10 b=10.3 c=codegnan
>>> print('a=%d b=%.2f c=%s' %(a,b,c))
...    
a=10 b=10.30 c=codegnan
>>> #.dot format
...    
>>> print('a={}| b={} | c={}' .format(a,b,c))
...    
a=10| b=10.3 | c=codegnan
>>> print('a={} |b={} | c={}'. format(c,a,b))
...    
a=codegnan |b=10 | c=10.3
>>> print('a={1} | b={2} | c= {0}'.format(a,b,c))
...    
a=10.3 | b=codegnan | c= 10
