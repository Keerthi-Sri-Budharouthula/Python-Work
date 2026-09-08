import json


with open("data.json",'r') as file:
    data = json.load(file)

data["username"]="bhanu"
data["skills"].append("mysql")

with open("data.json",'w') as file:
    json.dump(data,file,indent=4)
    
student={

    "name":"sajid",
    "age":22,
    "course":"Python"

}

json_data=json.dumps(student)

print(json_data)

student = json.loads(json_data)
print(student)
print(type(student))
