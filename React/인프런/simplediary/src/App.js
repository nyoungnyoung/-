import { useState, useRef } from "react";
import "./App.css";
import DiaryEditor from "./component/DiaryEditor";
import DiaryList from "./component/DiaryList";
import Lifecycle from "./component/Lifecycle";

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

  const onCreate = (author, content, emotion) => {
    const created_date = new Date().getTime();
    const newItem = {
      author,
      content,
      emotion,
      created_date,
      id: dataId.current,
    };
    dataId.current += 1; // id값에 +1
    setData([newItem, ...data]); // 새로 추가한 내용을 제일 위에 넣어주고, 원래 데이터까지 불러오기
  };

  const onRemove = (targetId) => {
    console.log(`${targetId + 1}번째 일기가 삭제되었습니다.`);
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

  return (
    <div className="App">
      <Lifecycle />
      <DiaryEditor onCreate={onCreate} />
      <DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} />
    </div>
  );
}

export default App;
