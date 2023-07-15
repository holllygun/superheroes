import requests
url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
response = requests.get(url).json()
count, superhero = 0, ''
for inf in response:
    for v in inf.values():
        if v == 'Hulk' or v == 'Captain America' or v == 'Thanos':
            a = inf['powerstats']['intelligence']
            if a >= count:
                count, superhero = a, v

print(f'The most intelligent superhero is {superhero}\nintelligence:{count}')

