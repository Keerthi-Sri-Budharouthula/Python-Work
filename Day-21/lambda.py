greater = lambda a,b:a if a>b else b
print(greater(12,13))
print(greater(20,50))
print(greater(80,29))

wish= lambda name: f'Welcome to the course{name}'
print(wish('rishi'))
print(wish('suma'))

iseven= lambda n:"Even" if n%2==0 else "Odd"
print(iseven(6))
print(iseven(7))
print(iseven(5))

avg=lambda a,b,c: (a+b+c)/3
print(avg(5,6,8))
print(avg(55,66,88))


domain = lambda mail:(mail.split('@')[-1]).split('.')[0]
print(domain('sai@gmail.com'))
print(domain('siri@codegnan.com'))
print(domain('swamy@outlook.com'))
print(domain('keethi@yahoo.com'))


gst = lambda price : price+price*0.18

print(gst(10000))
print(gst(1000))
print(gst(2000))
print(gst(100))


prices =[6236,213,21,298,409,1600]
res=list(map(lambda price : price+price*0.18,prices))
print(res)


names=['shiva','karthik','phani','mani']
res=list(map(lambda name: name.title(),names))
print(res)

prices=[7474,2417746,43178,7497,4848]
res= list(map(lambda price: price-price*0.3,prices))
print(res)

prices=[7474,2417746,43178,7497,4848]
res= list(filter(lambda price: price>5000,prices))
print(res)

prices=[7474,2417746,43178,7497,4848]
res= list(filter(lambda price: price%2!=0,prices))
print(res)

names =['shiva','karthik','phani','mani']
res= list(filter(lambda name: len(name)>5,names))
print(res)

from functools import reduce
l=[1,4,3,4,2,75,5235,87894]
res= reduce(lambda sum,i:sum+i,l)
print(res)

names =['shiva','karthik','phani','mani']
res=reduce(lambda res, i: res+' '+i,names)
print(res)


products={'sugar':60, 'salt':50, 'eggs':90, 'cooking oil':120,'bread':45}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))

print(dict(sorted(products.items(), key=lambda i:i[1])))
print(dict(sorted(products.items(), key=lambda i:i[1],reverse=True)))























