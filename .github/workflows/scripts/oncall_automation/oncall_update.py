import json
print("Running oncall automation")

# read json file
with open('data/teams/teams.json', 'r') as file:
    data = json.load(file)

print(data)