##### Q6. 이것은 프로그램 내에서 인스턴스가 오직 하나만 생성되는 것을 보장하고, 프로그램 어디서든 이 인스턴스로의 접근을 허용하는 것입니다. 이 패턴은 무엇일까요? (영문, 0000 pattern)

# 선택PJT20 - SSAFY 스무고개

REST 통신에 대해 이해하고, 인터페이스에 맞게 서버와 통신하는 법 학습
프론트/백엔드 모두가 REST통신을 사용기 때문에, 웹개발을 하는
개발자라면 반드시 익혀둘 필요가 있다.

### 과제 목표

* REST 통신의 구현 : 코드 구현

* 서버와 interface에 맞게 통신해보기 : REST통신 시도 & 서버 응답 확인

* 문제를 보고 설명에 맞는 정답을 REST 통신으로 제출하기
  
  * REST 통신으로 정답 제출, 다음 문제 풀기
  
  * 이 때 서버로부터 받은 리턴은 기록해 두어야 함

---------------

### ❓ REST 통신

참고 [[Network] REST란? REST API란? RESTful이란? - Heee's Development Blog](https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html)

##### REST의 정의

* **"Reapresentational State Transfer"** 의 약자  
  
  * 자원(resource)의 표현(representation)에 의한 상태 전달
  
  * 자원 : 해당 소프트웨어가 관리하는 모든 것
  
  * 자원의 표현 : 자원을 표현하기 위한 이름
  
  * 상태 전달 : json / xml을 통해 데이터를 전달하는 것이 일반적

* HTTP URI을 통해 자원을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미함

##### REST의 장단점

* 장점
  
  * HTTP 프로토콜의 인프라를 그대로 사용하므로 REST API 사용을 위한 별도의 인프라를 구출할 필요가 없다.
  
  * HTTP 프로토콜의 표준을 최대한 활용하여 여러 추가적인 장점을 함께 가져갈 수 있게 해준다.
  
  * HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능하다.
  
  * Hypermedia API의 기본을 충실히 지키면서 범용성을 보장한다.
  
  * REST API 메시지가 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악할 수 있다.
  
  * 여러가지 서비스 디자인에서 생길 수 있는 문제를 최소화한다.
  
  * 서버와 클라이언트의 역할을 명확하게 분리한다.

* 단점
  
  * 표준이 존재하지 않는다.
  
  * 사용할 수 있는 메소드가 4가지 밖에 없다.
  
  * 브라우저를 통해 테스트할 일이 많은 서비스라면 쉽게 고칠 수 있는 URL보다 Header 값이 더 어렵게 느껴진다.
  
  * 구형 브라우저가 아직 제대로 지원해주지 못하는 부분이 존재한다.
    
    * PUT, DELETE를 사용하지 못하는 점
    
    * pushState를 지원하지 않는 점

##### REST의 구성요소

* 자원(Resource) : URI
  
  * 모든 자원에는 고유한 ID가 존재하고, 이 자원은 서버에 존재함
  
  * 자원을 구별하는 ID는 '/groups/:group_id'와 같은 HTTP URI
  
  * Client는 URI의 이용해 자원을 지정하고 자원의 상태에 대한 조작을 서버에 요청함

* 행위(Verb) : HTTP Method
  
  * HTTP프로토콜의 Method(POST, GET, PUT, DELETE)를 사용함

* 표현(Representation of Resource)
  
  * Client가 자원의 상태(정보)에 대한 조작을 요청할 경우 서버가 이에 대한 응답으로 제공하는 것
  
  * REST에서 자원은 jso, xml, text, rss등 여러 형태의 representation으로 나타날 수 있으나, json/xml을 통해 데이터를 주고 받는 것이 일반적

##### REST 특징

* Server-Client 구조
  
  * 자원을 갖고 있는 쪽이 Server, 자원을 요청하는 쪽이 Client
  
  * REST Server : API 제공, 비즈니스 로직 처리 및 저장
  
  * Client : 사용자 인증이나 context(세선, 로그인 정보)를 직접 관리
  
  * 서로 간 의존성이 줄어듬

* Stateless (무상태)
  
  * HTTP 프로토콜이 무상태 프로토콜이므로 REST역시 동일함
  
  * Client의 context를 서버에 저장하지 않음
  
  * 서버는 각각의 요청을 완전히 별개의 것으로 인식하고 처리함

* Casheable (캐시 처리 가능)
  
  * HTTP 프로토콜을 그대로 사용하므로 웹에서 사용하는 기존 인프라 그대로 활용 가능 → 캐싱 기능 적용 가능
  
  * Last-Modified 태그나 E-Tag 이용해 캐싱 구현 가능
  
  * 대량 요청을 효율적으로 처리하기 위해 캐시가 요구됨

* Layered System (계층화)
  
  * Client는 REST API 서버만 호출
  
  * RESST 서버는 다중 계층으로 구성될 수 있음

* Code-On-Demand (optional)
  
  * 서버로부터 스크립트를 받아 Client에서 실행가능

* 인터페이스 일관성
  
  * URI로 지정한 Resource에 대한 조작을 통일되고 한정적인 인터페이스로 수행
  
  * HTTP 표준 프로토콜을 따르는 모든 플랫폼에서 사용 가능

-----------------------

### 🛠 Python을 이용한 REST 통신 구현

##### Requests

HTTP 통신을 위한 파이썬 라이브러리

##### Requests 기본 사용법

```python
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code        # 200
r.headers['content-type']        #'application/json; charset=utf8'
r.encoding           # 'utf-8'
r.text               # u'{"type":"User"...}'
r.json()             # {u'private_gists':419, u'total_private_repos':77, ...}
```

##### 다른 Method 사용법

```python
import requests
r = requests.get('https://api.github.com/events')
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
```

##### json 요청하고 파싱하기

```python
import requests
url = 'https://gist.githubusercontent.com/TWpower/771f9dfc8d9e1ddc0ecbdaea5b2e379e/raw/2c7785b4835138255bdadb71bd83702e53ac2677/test-example.json'

data = requests.get(url).json()
```

json파일을 HTTP요청을 통해서 받아오고, 이를 python에서 사용할 수 있는 dictionary 형태로 파싱하는 코드

--------

### ✨ 과제 리턴값

##### Q1. SSAFY의 인스타그램 계정명은 무엇일까요? (영문)

**→ hellossafy**

```json
{
    'code': 200, 
    'question': 'Q2: 깊이 우선 탐색의 영문 약자는?',
    'nextUrl': 'bravo'
}
```

##### Q2.  깊이 우선 탐색의 영문 약자는?

**→ dfs**

```json
{
    'code': 200, 
    'question': 'Q3: SSAFY의 인스타그램에는 SSAFY의 여러
                모습들이 올라와 있는데요. SSAFY의 소식을
                전해주는 기자단의 영문 명칭은 무엇일까요?',
    'nextUrl': 'chopper'
}
```

##### Q3. SSAFY의 인스타그램에는 SSAFY의 여러 모습들이 올라와 있는데요. SSAFY의 소식을 전해주는 기자단의 영문 명칭은 무엇일까요?

**→ ssafycial**

```json
{
    'code': 200, 
    'question': 'Q4: 교차 출처 리소스 공유
                (Cross Origin Resource Sharing)는 추가적인
                http 헤더를 이용하여, 한 출처에서 실행 중인
                웹 애플리케이션이 다른 출처의 자원에 접근할 수
                있는 권한을 부여하도록 브라우저에 알려주는 것을
                말합니다. 자원의 출처가 다르다는 것은 3가지
                요소를 가지고 파악하는데요.3가지 요소에는
                domain, port, 그리고 이것이 있습니다.
                이것은 무엇일까요? (영문)',
    'nextUrl': 'weekend'
} 
```

##### Q4. 교차 출처 리소스 공유(Cross Origin Resource Sharing)는 추가적인 http 헤더를 이용하여, 한 출처에서 실행 중인 웹 애플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 것을 말합니다. 자원의 출처가 다르다는 것은 3가지 요소를 가지고 파악하는데요. 3가지 요소에는 domain, port, 그리고 이것이 있습니다. 이것은 무엇일까요? (영문)

**→ protocol**

```json
{
    'code': 200, 
    'question': 'Q5: 이것은 경량의 데이터 교환 형식으로,
                사람과 기계가 읽고 쓰기에 용이하며, Javascript
                객체 문법으로 구조화된 데이터를 표현하기 위한
                문자 기반의 데이터 포맷이다. 객체를 나타낼 때
                중괄호로 시작해서 중괄호로 끝나는 이것은
                무엇인가? (영문, 약자)',
    'nextUrl': 'river'
}
```

##### Q5. 이것은 경량의 데이터 교환 형식으로, 사람과 기계가 읽고 쓰기에 용이하며, Javascript 객체 문법으로 구조화 된 데이터 포맷이다. 객체를 나타낼 때 중괄호로 시작해서 중괄호로 끝나는 이것은 무엇인가? (영문, 약자)

**→ json**

```json
{
    'code': 200, 
    'question': 'Q6: 이것은 프로그램 내에서 인스턴스가 오직
                하나만 생성되는 것을 보장하고, 프로그램 어디서든
                이 인스턴스로의 접근을 허용하는 것입니다.
                이 패턴은 무엇일까요?(영문, OOOO pattern)',
    'nextUrl': 'hand'
}
```

##### Q6. 이것은 프로그램 내에서 인스턴스가 오직 하나만 생성되는 것을 보장하고, 프로그램 어디서든 이 인스턴스로의 접근을 허용하는 것입니다. 이 패턴은 무엇일까요? (영문, 0000 pattern)

**→ singleton**

```json
{
    'code': 200, 
    'question': 'Q7: 브라우저에 데이터를 저장하는 방법에는
                storage, indexed DB, 그리고 이것이 있습니다.
                session ID를 저장하는 용도로도 사용되는 이것은
                무엇일까요? (영문)',
    'nextUrl': 'over'
}
```

##### Q7. 브라우저에 데이터를 저장하는 방법에는 storage, indexed DB, 그리고 이것이 있습니다. session ID를 저장하는 용도로도 사용되는 이것은 무엇일까요? (영문)

**→ cookie**

```json
{
    'code': 200, 
    'question': 'Q8: 이것은 Remote Dictionary Server의
                약자로, 키-값 구조의 비정형 데이터를 저장하고
                관리하기 위한 오픈 소스 비관계형 DBMS다.
                인스타그램, LINE 등에서 널리 사용되는 이것은?
                (영문)',
    'nextUrl': 'hello'
}
```

##### Q8. 이것은 Remote Dictionary Server의 약자로, 키-값 구조의 비정형 데이터를 저장하고 관리하기 위한 오픈 소스 비관계형 DBMS다. 인스타그램, LINE 등에서 널리 사용되는 이것은? (영문)

**→ redis**

```json
{
    'code': 200, 
    'question': 'Q9: 이것은 디자인 패턴의 하나로
                Model + View + View Model을 합친 말이다. 
                View와 Model 사이에 의존성을 없애고 모듈화를
                가능하게 만든 이것은?(영문, OOOO pattern)',
    'nextUrl': 'python'
}
```

##### Q9. 이것은 디자인 패턴의 하나로 Model + View + View Model을 합친 말이다. View와 Model 사이에 의존성을 없애고 모듈화를 가능하게 만든 이것은? (영문, OOOO pattern)

**→ mvvm**

```json
{
    'code': 200, 
    'question': 'Q10: 이것은 파이썬의 라이브러리로 데이터 조작
                및 분석을 위해서 주로 사용된다. pd라는 약어로
                주로 사용되는 이것은? (영문)', 
    'nextUrl': 'java'
}
```

##### Q10. 이것은 파이썬의 라이브러리로 데이터 조작 및 분석을 위해서 주로 사용된다. pd라는 약어로 주로 사용되는 이것은? (영문)'

**→ pandas**

```json
{
    'code': 200, 
    'question': 'Q11: 이것은 근거리 무선 통신 기술의 하나로
                2.4Ghz 대역폭을 사용한다. 갤럭시 버즈와 같은
                무선 이어폰에 주로 사용되며, 덴마크의 왕인
                하랄 블로탄의 이름에서 유래한 이것은? (영문)', 
    'nextUrl': 'script'
}
```

##### Q11. 이것은 근거리 무선 통신 기술의 하나로 2.4Ghz 대역폭을 사용한다. 갤럭시 버즈와 같은 무선 이어폰에 주로 사용되며, 덴마크의 왕인 하랄 블로탄의 이름에서 유래한 이것은? (영문)

**→ bluetooth**

```json
{
    'code': 200, 
    'question': 'Q12: SSAFY 1기 교육생들이 출시한 앱으로,
                삼성전자 해외연구소 파견 교육과정 중 우크라이나
                팀에서 개발한 헬스케어 앱의 이름은? (영문)',
    'nextUrl': 'zero'
}
```

##### Q12. SSAFY 1기 교육생들이 출시한 앱으로, 삼성전자 해외연구소 파견 교육과정 중 우크라이나 팀에서 개발한 헬스케어 앱의 이름은? (영문)

**→ fittymon**

```json
{
    'code': 200, 
    'question': 'Q13: In computing, this is an optimization
                technique used primarily to speed up
                computer programs by storing results of
                expensive function calls and returning the
                cached result when the same inputs occur
                again. What is this? (영문)', 
    'nextUrl': 'coat'
}
```

##### Q13. In computing, this is an optimization technique used primarily to speed up computer programs by storing results of expensive function calls and returning the cached result when the same inputs occur again. What is this? (영문)

**→ memoization**

```json
{
    'code': 200, 
    'question': 'Q14: 전통적인 프로그래밍에서는 개발자가 작성한
                프로그램이 외부 라이브러리 코드를 호출한다.
                그러나 이것이 적용된 구조에서는 외부 라이브러리
                코드가 개발자가 작성한 코드를 호출한다.
                이것은 무엇인가? (영문, 약자로 쓰시오)',
    'nextUrl': 'sand'
}
```

##### Q14. 전통적인 프로그래밍에서는 개발자가 작성한 프로그램이 외부 라이브러리 코드를 호출한다. 그러나 이것이 적용된 구조에서는 외부 라이브러리 코드가 개발자가 작성한 코드를 호출한다. 이것은 무엇인가? (영문, 약자로 쓰시오)

**→ ioc (Inversion of Control)**

```json
{
    'code': 200, 
    'question': 'Q15: 이것은 리눅스의 응용 프로그램들을
                소프트웨어 컨테이너 안에 배치시키는 일을
                자동화하는 오픈 소스이다. 리눅스에서 운영체제
                수준 가상화의 추상화 및 자동화 계층을 추가적으로
                제공하기도 하는 이것은 무엇인가? (영문)', 
    'nextUrl': 'king'
}
```

##### Q15. 이것은 리눅스의 응용 프로그램들을 소프트웨어 컨테이너 안에 배치시키는 일을 자동화하는 오픈 소스이다. 리눅스에서 운영체제 수준 가상화의 추상화 및 자동화 계층을 추가적으로 제공하기도 하는 이것은 무엇인가? (영문)

**→ docker**

```json
{
    'code': 200, 
    'question': 'Q16: 루트 노드에서 시작해서 다음 분기로
                넘어가기 전에 해당 분기를 완벽하게 탐색하는
                방법으로, 미로를 탐색할 때 한 방향으로 갈 수
                있을 때까지 계속 가다가 더 이상 갈 수 없게 되면
                다시 가장 가까운 갈림길로 돌아와서 다른 방향으로
                다시 탐색을 진행하는 것과 유사한 이것은?
                (영문 3글자, 약자로 쓰시오)',
    'nextUrl': 'knight'
}
```

##### Q16. 루트 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법으로, 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 다른 방향으로 다시 탐색을 진행하는 것과 유사한 이것은? (영문 3글자, 약자로 쓰시오)

**→ dfs**

```json
{
    'code': 200, 
    'question': 'Q17: 삼성 갤럭시 Z 플립은 안드로이드
                스마트폰으로 폴더블 디스플레이를 탑재했다.
                갤럭시 Z 플립의 개발 코드 네임은? (영문)',
    'nextUrl': 'great'
}
```

##### Q17. 삼성 갤럭시 Z 플립은 안드로이드 스마트폰으로 폴더블 디스플레이를 탑재했다. 갤럭시 Z 플립의 개발 코드 네임은? (영문)

**→ bloom**

```json
{
    'code': 200, 
    'question': 'Q18: SSAFY의 공식 영문 명칭에서 가장 많이
                등장하는 알파벳은? (영문)',
    'nextUrl': 'again'
}
```

##### Q18. SSAFY의 공식 영문 명칭에서 가장 많이 등장하는 알파벳은? (영문)

**→ a**

```json
{
    'code': 200, 
    'question': 'Q19: 이 정렬 방법은 토니 호어가 고안한
                방법으로, 다른 원소와의 비교만으로
                정렬을 수행하는 비교 정렬 방법의 하나이다.
                평균적으로 O(n log n)의 시간복잡도를 가지는
                이 정렬은 무엇인가? (영문, OOO sort)',
    'nextUrl': 'ring'
}
```

##### Q19. 이 정렬 방법은 토니 호어가 고안한 방법으로, 다른 원소와의 비교만으로 정렬을 수행하는 비교 정렬 방법의 하나이다. 평균적으로 O(n log n)의 시간복잡도를 가지는 이 정렬은 무엇인가? (영문, OOO sort)

**→ quick**

```json
{
    'code': 200, 
    'question': 'Q20: 이것은 컨테이너화된 애플리케이션의
                자동 배포, 스케일링 등을 제공하는 관리시스템으로
                오픈 소스이다. 구글에 의해 설계되었고, 리눅스
                재단에 의해 관리되고 있으며 도커와 같은 컨테이너
                도구와 함께 동작하는 이것은 무엇인가? (영문)',
    'nextUrl': 'jordan'
}
```

##### Q20. 이것은 컨테이너화된 애플리케이션의 자동 배포, 스케일링 등을 제공하는 관리시스템으로 오픈 소스이다. 구글에 의해 설계되었고, 리눅스 재단에 의해 관리되고 있으며 도커와 같은 컨테이너 도구와 함께 동작하는 이것은 무엇인가? (영문)

**→ kubernetes**

```json
{
    'code': 200, 
    'question': 'question': '모든 문제를 완료하셨습니다.', 
    'nextUrl': '수고하셨습니다.'
}
```
