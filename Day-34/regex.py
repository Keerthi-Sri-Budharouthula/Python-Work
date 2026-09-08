import re 
'''
pattern = r'[0-9]'
text = 'codegnan2026 python version 3.14'

res = re.search(pattern,text)
res = re.match(pattern,text)
print(res.group() if res else "Pattern not found")

res = re.findall(pattern,text)
print(res)

res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())

pattern = r'[0-9]{10}'
text ='9876543210'
res = re.fullmatch(pattern,text)#check macth
print(res)


pattern=r'[,(#]'
text='java,python(html#css'
res=re.split(pattern,text)#separate
print(res)

pattern=r'[a-z]'
text='python version 3.14, batch-63'
res=re.sub(pattern,'*',text)#replace 
print(res)

pattern=r'e.t'
text='e@t eaat eat eet ett ect Egfhjet hgjeokj'

pattern=r'^91'
text='919876543210'
res=re.findall(pattern,text) 
print(res)

pattern=r'0$'
text='919876543210'
res=re.findall(pattern,text) 
print(res)

pattern=r'to+'#one or more occurance
text='to tggnjjuugj too tooo toooooo'
res=re.findall(pattern,text) 
print(res)

pattern=r'to*'#zero or more occurance
text='to tggnjjuugj too tooo toooooo'
res=re.findall(pattern,text) 
print(res)

pattern=r'ab+'
text='ab abbb a abbbbbb abbbb'
res=re.findall(pattern,text) 
print(res)

pattern=r'ab*'
text='ab abbb a abbbbbb abbbb'
res=re.findall(pattern,text) 
print(res)

pattern=r'91|0'
text='05678'
res=re.findall(pattern,text) 
print(res)
'''
pattern=r'[aeiouAEIOU]'
text='Codegnan Programming'
res=re.findall(pattern,text) 
print(res)












