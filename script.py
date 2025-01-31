import requests

res = requests.get('https://scotch.io')

print(res)

if res:
    print('Response OK')
else:
    print('Response Failed')

print(res.status_code)
print(res.headers)
print(res.text)

API_KEY = 'your yandex api key'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
res = requests.get(url)
params = dict(key=API_KEY, text='Hello', lang='en-es')
res = requests.get(url, params=params)
print(res.text)
params = dict(key=API_KEY, text='Hello', lang='en-fr')
print(res.headers)
json = res.json()
print(json)
print(json['text'])
print(json['text'][0])
params = dict(key=API_KEY, text='Goodbye', lang='en-es')