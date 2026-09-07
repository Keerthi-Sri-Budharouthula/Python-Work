'''budget = int(input("enter the budget: "))

if budget>10000:
    print("trip")
elif budget>5000:
    print("resort stay")
elif budget>3000:
    print("movie and dinner")
elif budget>1000:
    print("cafe and shopping")
elif budget>500:
    print("street food and park visit")
else:
    print("stay home")
    

hour= int(input("enter the hour:"))
if 5<=hour<=11 : # hour>=5 and hour<=11
    print("Good morning")
elif 12<=hour<=16:
    print("Good afternoon")
elif 17<=hour<=20:
    print("Good evening")
else:
    print("Good night")
    '''

budget = int(input())
if budget > 10000:
    print("Cloud Hosting")
elif budget > 5000 :
    print("Bussiness Hosting")
elif budget > 2000 :
    print("Premium Hosting")
else:
    print("Single Hosting")
    