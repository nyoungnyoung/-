import React, { useEffect, useState } from "react"

// TextView는 text가 변했을때만 리렌더 되면 되고, CountView도 동일한데
// 지금은 뭐가 변하든 둘다 같이 리렌더 되는 상황임..!
// 그래서 필요한게 컴포넌트 재사용! react.memo!
// 전달받는 props(text/count)가 변하지 않으면 절대 재렌더링이 되지 않게 됨!

// const TextView = React.memo(({text}) => {
//     useEffect(() => {
//         console.log(`Update :: Text : ${text}`)
//     })
//     return (
//         <div>{text}</div>
//     )
// })

// const CountView = React.memo(({count}) => {
//     useEffect(() => {
//         console.log(`Update :: count : ${count}`)
//     })
//     return (
//         <div>{count}</div>
//     )
// })


////////////////////////////////////////////////
// 엥? A버튼 누르면 콘솔에 아무것도 안찍히는데 B버튼 누르면 콘솔에 상태가 찍힌다..?
// 왜그럴까? B버튼을 누를 때 전달되는 props인 obj가 객체이기 때문임!!
// 자바스크립트는 기본적으로 객체를 비교할 때 얕은 비교를 하기 때문에 이런 문제가 발생함! 
const CounterA = React.memo(({count}) => {
    useEffect(() => {
        console.log(`counterA Update - count : ${count}`)
    })
    return (
    <div>{count}</div>
 )   
})

const CounterB = React.memo(({obj}) => {
    useEffect(() => {
        console.log(`CounterB Update - count : ${obj.count}`)
    })
    return (
        <div>{obj.count}</div>
    )
})

////////////////////////////////////////////////
// 객체를 제대로 비교해주려면 어떻게 해야할까?
const areEqual = (preProps, nextProps) => {
    // if (preProps.obj.count === nextProps.obj.count){
    //     return true // 이전 프롭스와 현재 프롭스가 같다 -> 리렌더링을 일으키지 않는다.
    // }
    // return false // 이전 프롭스와 현재 프롭스가 같지 않다 -> 리렌더링을 일으킴
    return preProps.obj.count === nextProps.obj.count
}

// 이렇게 하면 areEqual 함수가 React.memo 함수의 비교함수로 작용하게 됨!
const MemoizedCounterB = React.memo(CounterB, areEqual)


const OptimizeTest = () => {
    const [count, setCount] = useState(1);
    // const [text, setText] = useState("");
    const [obj, setObj] = useState({
        count: 1
    })

    return (
        <div style={{padding:50}}>
            {/* <div>
                <h2>count</h2>
                <CountView count={count}/>
                <button onClick={() => setCount(count+1)}>+</button>
            </div>
            <div>
                <h2>text</h2>
                <TextView text={text}/>
                <input value={text} onChange={(e) => setText(e.target.value)} />
            </div> */}

            {/* 아래 예시의 경우 onClick 이벤트로 set함수가 실행되면서, 기존과 똑같은 값을 할당시키게 됨! */}
            <div>
                <h2>Counter A</h2>
                <CounterA count={count}/>
                <button onClick={() => setCount(count)}>A button</button>
            </div>
            <div>
                <h2>Counter B</h2>
                <MemoizedCounterB obj={obj}/>
                {/* <CounterB obj={obj}/> */}
                <button onClick={() => setObj({
                    count: obj.count
                })}>B button</button>
            </div>
        </div>
    )
}

export default OptimizeTest