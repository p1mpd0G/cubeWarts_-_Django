import requests

res = requests.get('https://scotch.io')

print(res)

if res:
    print('Response OK')
else:
    print('Response Failed')