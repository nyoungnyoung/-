# 필수PJT5 - 비동기 프로그래밍

-----------

일반적으로 프로그램 함수는 순차적으로 실행된다.(동기식) 하지만 많은 시간이 걸리는 작업의 경우(ex.대용량 파일 업로드) 그것이 완료될 때 까지 다음 함수를 실행하지 못하는 Blocking 상태에 빠지게 된다. 비동기식은 이 문제를 피할 수 있게 해 준다. 이번 과제는 비동기식 프로그래밍을 이해하고, 자유롭게 구현하는 능력을 갖출 수 있게 도와줄 것이다.

-------

### 비동기함수

```javascript
function delay_word(word, delay) {
  return new Promise(resolve => {
    setTimeout(function (){
      resolve(word)
    }, delay)
  })
}
```

delay만큼 기다린 후 입력 값 word 그대로 return 하는 간단한 비동기 함수

----

### Chaining 처리

하나 또는 두 개 이상의 비동기 작업을 **순차적으로** 실행하는 상황이다.
이전 비동기 작업이 완료된 후 다음 작업을 순차적으로 실행한다.

#### Hard Code

* **promise_hard_code** : promise 코드

```javascript
delay_word('SAMSUNG', 500).then((resolve) => {

    console.log(resolve)

    delay_word('SW', 490).then((resolve) => { 

        console.log(resolve)

        delay_word('ACADEMY', 480).then((resolve) => {

            console.log(resolve)

            delay_word('FOR', 470).then((resolve) => {

                console.log(resolve)

                delay_word('YOUTH', 460).then((resolve) => {

                    console.log(resolve)
                })
            })
        })
    })
})
```

* **await_hard_code** : async / await 코드

```javascript
async function test(){
    const resolve_0 = await delay_word('SAMSUNG', 500)
    console.log(resolve_0)
    const resolve_1 = await delay_word('SW', 490)
    console.log(resolve_1)
    const resolve_2 = await delay_word('ACADEMY', 480)    
    console.log(resolve_2)
    const resolve_3 = await delay_word('FOR', 470)
    console.log(resolve_3)
    const resolve_4 = await delay_word('YOUTH', 460)
    console.log(resolve_4)
}
```

#### Soft Code

비동기함수 호출 횟수나 입력값이 **가변적**이라면 Soft Code로 구현해야 함

* **promise_soft_code**

```javascript
const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]

array.reduce((prev, item) => {

    return prev.then(() =>
        delay_word(item.word, item.delay).then((promise) => {console.log(promise)}))

}, Promise.resolve())
```

* **await_soft_code**

```javascript
const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]

async function test(){

    for(const item of array) {
        const resolve = await delay_word(item.word, item.delay)

        console.log(resolve)                
    }
}
```

-------------------

### All 처리, 비순차 결과

이전 비동기 작업이 다음 비동기 작업에 영향을 주지 않을 경우,
**이전 비동기함수 작업이 끝나기 전에 현재 작업을 실행**해도 무방하다.
이 때 함수 호출 순서와 상관 없이 먼저 **작업이 끝나는 순으로 결과를
받는(비순차결과)** 코드이다. 

* **promise_all_non_sequence**

```javascript
const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]


array.forEach(async (item) => {

    delay_word(item.word, item.delay).then((resolve) => {console.log(resolve)})            
})
```

* **await_all_non_sequence**

```javascript
const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]


array.forEach(async (item) => {

    const resolve = await delay_word(item.word, item.delay)

    console.log(resolve)

})
```

------

### All 처리, 순차 결과

**All처리**를 하되, 순차적으로(**함수 작업이 끝나는 순으로**) 결과를 출력한다.

* **promise_all_sequence**

```javascript
const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]

const promise_list = []

array.forEach((item) => {

    const promise = delay_word(item.word, item.delay)

    promise_list.push(promise)
})

Promise.all(promise_list).then((values) => {

    values.forEach((resolve) => {console.log(resolve)})
})
```

* **await_all_sequence**

```javascript
const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]


async function test(){

    const async_fun_list = []

    for(item of array){    

        const async_fun = delay_word(item.word, item.delay)

        async_fun_list.push(async_fun)
    }

    for(async_fun of async_fun_list){

        const resolve = await async_fun

        console.log(resolve)
    }        
}
```


