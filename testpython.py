import json
json_data=open("data/testdata.txt").read()

data = json.loads(json_data)
print(data)
