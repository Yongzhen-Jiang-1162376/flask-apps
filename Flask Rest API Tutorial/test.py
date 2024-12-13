import requests


BASE = 'http://localhost:5000/'

# headers = {'accept': 'application/json'}

data = [
    {'likes': 78, 'name': 'Joe', 'views': 10000},
    {'likes': 1000, 'name': 'How to make REST API', 'views': 80000},
    {'likes': 35, 'name': 'Tim', 'views': 2000}
]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()

response = requests.get(BASE + 'video/1')
print(response.json())
