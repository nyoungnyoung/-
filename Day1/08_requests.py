import requests

# http 요청을 생성한다
url = 'https://api.agify.io/?name=symon'
response = requests.get(url).json()
name = response.get('name')
age = response.get('age')
count = response.get('count')

print(f'이름 : {name} 나이 : {age} 카운트 : {count}')


