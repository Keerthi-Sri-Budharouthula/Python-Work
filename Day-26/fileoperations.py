file=open('pfs-63.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

with open('pfs-63.txt','r') as file:  #recommended format for file operations
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()
    

with open('mysql.txt','w') as file:#automatically create new file and write content
    file.write("DDL,DML,DQL")

with open('pfs-63.txt','w') as file: #overridden the content
    file.write("Shifted to Branch-1")


with open('pfs-63.txt','a') as file: #it not overridden only add the content at end
    file.write("  only for today")


with open('pfs-63.txt','a+') as file:#to perform two opeartions append and read
    file.write(" Tom same branch 5")
    file.seek(0)
    print(file.read())


with open('pfs-63.txt','r+') as file:#to perform two opeartions read and append
    print(file.read())
    file.write(" classes as usual")


with open('pfs-63.txt','w+') as file:#to perform two opeartions write and read
    
    file.write("Afternoon holiday")
    file.seek(0)
    print(file.read())
    
    





































































