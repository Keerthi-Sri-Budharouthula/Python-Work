'''
fa = eval(input("Follows Account: "))
cf = eval(input("Close Friend: "))

if fa:
    if cf:
        print("Story Visible")
    else:
        print("Not in close friends list")
else:
    print("Follow the Account First")
    

player=eval(input("Registered: "))

if player:
    fee=eval(input("Fee Paid: "))
    if fee:
        print("Tournament Entry Confirmed")
    else:
        print("Entry fee pending")
else:
    print("registration pending")
'''

link=eval(input("File link Active:"))
if link:
    permission=eval(input("access permission is granted:"))
    if permission:
        print("FIle Opened Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")
