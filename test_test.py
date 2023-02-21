import json

with open("./test.json", "r") as f:
    data = json.load(f)
    # convert data to string
    data = json.dumps(json.dumps(data))
    print(data)