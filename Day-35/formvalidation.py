import re
'''
fullname=input("Enter the full name: ")
pattern=r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res=re.fullmatch(pattern,fullname)
print("Valid full name" if res else "Invalid full name")


email=input("Enter the email: ")
pattern=r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+.[a-zA-z]{2,}$
res=re.fullmatch(pattern,email)
print("Valid mail" if res else "Invalid mail")


phonenumber=input("Enter the phone number: ")
pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
res=re.fullmatch(pattern,phonenumber)
print("Valid phone number" if res else "Invalid phone number")


password=input("Enter the password: ")
pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-za-z\d@$!%*?&]{8,}'
res = re.fullmatch(pattern,password)
print("Valid password" if res else "Invalid password")


password=input("Enter the password: ")
pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-za-z\d@$!%*?&]{8,}'
res = re.fullmatch(pattern,password)
print("Valid password" if res else "Invalid password")
'''


username = input("Enter username: ")
aadhaar = input("Enter Aadhaar number: ")
pan = input("Enter PAN number: ")

username_pattern = r'^[A-Za-z][A-Za-z0-9_]{2,19}$'
aadhaar_pattern = r'^\d{12}$'
pan_pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

print("Valid username" if re.fullmatch(username_pattern, username) else "Invalid username")
print("Valid Aadhaar" if re.fullmatch(aadhaar_pattern, aadhaar) else "Invalid Aadhaar")
print("Valid PAN" if re.fullmatch(pan_pattern, pan) else "Invalid PAN")
















































































