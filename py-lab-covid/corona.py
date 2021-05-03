import json

# file_handler = 

with open("data.json", 'r') as file_handler: 
    data = json.load(file_handler)

print(data)
for obj in data["data"[1]]:
    print(obj)["state"]