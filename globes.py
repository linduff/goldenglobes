import json

f = open('nominations.json')

data = json.load(f)

print(len(data))

for i in data:
    print(i['title'] + " - " + str(len(i['nominations'])) + " nominations")