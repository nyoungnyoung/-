import { useState, useRef, useEffect, useMemo, useCallback } from "react";
import "./App.css";
import DiaryEditor from "./component/DiaryEditor";
import DiaryList from "./component/DiaryList";
// import OptimizeTest from "./component/OptimizeTest";
// import Lifecycle from "./component/Lifecycle";

// const dummyList = [
//   {
//     id: 1,
//     author: "이정환",
//     content: "안녕하세요",
//     emotion: 3,
//     created_date: new Date().getTime(), // 시간 객체 생성(현재 시간 기준).숫자로 시간(밀리second) 반환
//   },
//   {
//     id: 2,
//     author: "홍길동",
//     content: "ㅎㅎㅎㅎㅎ",
//     emotion: 1,
//     created_date: new Date().getTime(),
//   },
//   {
//     id: 3,
//     author: "윤선영",
//     content: "오빠 보고싶당",
//     emotion: 5,
//     created_date: new Date().getTime(), // 시간 객체 생성(현재 시간 기준).숫자로 시간(밀리second) 반환
//   },
//   {
//     id: 4,
//     author: "박지우",
//     content: "뇽이 보고싶당",
//     emotion: 5,
//     created_date: new Date().getTime(), // 시간 객체 생성(현재 시간 기준).숫자로 시간(밀리second) 반환
//   },
// ];

function App() {

  const [data, setData] = useState([]);
  const dataId = useRef(0); // 데이터의 id 설정해주기 위한 변수

  // API 요청 주소 https://jsonplaceholder.typicode.com/comments
  // API 호출 함수 -> 내장 객체인 fetch 이용, await와 함께 사용해보자
  const getData = async() => {
    const res = await fetch('https://jsonplaceholder.typicode.com/comments').then((res) => res.json())
    
    const initData = res.slice(0,20).map((it) => {
      return {
        author : it.email,
        content : it.body,
        emotion : Math.floor(Math.random() * 5) + 1,  // emotion을 1부터 5까지 랜덤으로 뽑아올 수 있도록 Math이용해서 작성해줌
        created_date : new Date().getTime(),  // ms 단위로 생성시간..!
        id : dataId.current++ // 현재 dataId값으로 넣고 난 뒤에 +1 해주겠다는 뜻!
      }
    })
    setData(initData)
  }

  // App 컴포넌트가 Mount 되자마자 getData함수 호출하기!
  useEffect(() => {
    getData()
  }, [])

  const onCreate = useCallback((author, content, emotion) => {
    const created_date = new Date().getTime();
    const newItem = {
      author,
      content,
      emotion,
      created_date,
      id: dataId.current,
    };
    dataId.current += 1; // id값에 +1
    setData((data) => [newItem, ...data]); // 새로 추가한 내용을 제일 위에 넣어주고, 원래 데이터까지 불러오기
  }, []);

  const onRemove = (targetId) => {
    // console.log(`${targetId + 1}번째 일기가 삭제되었습니다.`);
    const newDiaryList = data.filter((it) => it.id !== targetId);
    // console.log(newDiaryList);
    setData(newDiaryList);
  };

  // 수정하기 기능
  const onEdit = (targetId, newContent) => {
    setData(
      // data의 모든 원소를 돌면서 해당 원소의 id와 targetId가 같은지 검사 -> 일치하면 수정의 대상이 되는것!
      // 수정의 대상이라면 content를 교체해 주고, 아니면 원래 데이터를 반환
      data.map((it) =>
        it.id === targetId ? { ...it, content: newContent } : it
      )
    );
  };

  // 최적화 1 - useMemo(연산 최적화, 연산 결과 재사용)
  // 감정 분석 함수 만들기 -> useMemo 사용해서 결과값 저장하기
  // useMemo(콜백함수, []) : 콜백함수가 리턴하는 값을 최적화할 수 있도록 도와줌
  // useMemo의 두번째 파라미터인 배열은 dependency array! 이 값이 변화할 때 콜백함수 실행
  // 주의해야 할 점! useMemo를 사용해서 어떤 함수를 최적화하면, 이는 더이상 함수가 아니다!
  // 콜백함수가 리턴하는 값을 그냥 리턴한다! 값으로 사용할 것!
  // 어떤 함수가 있고, 그 함수가 어떤 값을 리턴하고 있을 때! 리턴까지의 연산을 최적화 하고 싶다면
  // useMemo 사용해서 특정값(dependency array)이 변화할 때만 이 연산을 수행하도록 해 주면 된다.
  const getDiaryAnalysis = useMemo(
    () => {
    // console.log("일기 분석 시작")
    
    const goodCount = data.filter((it) => it.emotion >= 3).length; // 기분이 좋은 일기가 몇개인지 세 주기
    const badCount = data.length - goodCount;  // 전체 일기 개수에서 좋은 일기 개수 빼주기
    const goodRatio = (goodCount / data.length) * 100;
    return {goodCount, badCount, goodRatio}
  }, [data.length]
  );

  const {goodCount, badCount, goodRatio} = getDiaryAnalysis

  return (
    <div className="App">
      {/* <Lifecycle /> */}
      {/* <OptimizeTest/> */}
      <DiaryEditor onCreate={onCreate} />
      <div>전체일기 : {data.length}</div>
      <div>기분 좋은 일기 개수 : {goodCount}</div>
      <div>기분 나쁜 일기 개수 : {badCount}</div>
      <div>기분 좋은 일기 비율 : {goodRatio}</div>
      <DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} />
    </div>
  );
}

export default App;
