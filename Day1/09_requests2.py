# 요청URL : http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty
# 요청 파라미터 : 클라이언트에서 서버로 보내는 데이터
# 요청 파라미터를 추가하는 방법
# get요청 시 : URL?파라미터이름=파라미터값&파라미터이름=파라미터값&파라미터이름=파라미터값....
# get 요청 : 데이터를 서버에서 받아올 때 하는 요청
# post 요청 : 내가 가진 데이터를 서버에다가 저장할 때 하는 요청
# 필수값 : serviceKey/sidoName
# http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=8oEmCfzU8ysOPLoiFNOV1ri%2Ft8IqtnAsySTqKIlNXzHnk2NgLfCnmuurf1AHOw4H4PN%2FmHW6DbFrH82cJvOC1A%3D%3D&sidoName=대구&returnType=json
# https으로 시작하게 만들면 에러 뜸!

import requests

# http 요청을 생성한다
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=8oEmCfzU8ysOPLoiFNOV1ri%2Ft8IqtnAsySTqKIlNXzHnk2NgLfCnmuurf1AHOw4H4PN%2FmHW6DbFrH82cJvOC1A%3D%3D&sidoName=대구&returnType=json'
response = requests.get(url).json()

# print(type(response))

# for key in response.keys():
#     print(key)

#stationName' : '진천동'
result = response.get('response')
body = result.get('body')
items = body.get('items')
# print(type(items))

pm10Sum = 0    # 평균을 구하기 위해 총합을 저장하는 변수
cnt = 0    # 평균을 구하기 위해서 몇 개 더했는지 저장하는 변수
for item in items:
    # items 속성이 list임! [10, 12, 14, 15, ...]
    # item >>> 하나 하나가 dictionary : 동 정보, 미세먼지 정보를 포함
    if item.get('pm10Value') != '-':
        pm10Sum = pm10Sum + int(item.get('pm10Value'))
        cnt += 1
        # 미세먼지 농도(pm10Value) 정수 값으로 가져와서 변수 하나에 계속해서 더해줌!
        # item은 dict이기 때문에 get 사용할 수 있음!
        # item.get('pm10Value')로 가져온 값은 문자열이기 때문에 int함수로 정수화 해주기

dust = pm10Sum/cnt  # cnt 변수 선언 하지 않고 dust = pm10Sum/len(items) 해도 됨!
print(f'대구의 현재 평균 미세먼지 농도는 {dust}입니다.')
