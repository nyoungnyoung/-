import './App.css';
import DiaryEditor from './component/DiaryEditor';
import DiaryList from './component/DiaryList';

const dummyList = [
  {
    id: 1,
    author: "이정환",
    content: "안녕하세요",
    emotion: 3,
    created_date: new Date().getTime()     // 시간 객체 생성(현재 시간 기준).숫자로 시간(밀리second) 반환
  },
  {
    id: 2,
    author: "홍길동",
    content: "ㅎㅎㅎㅎㅎ",
    emotion: 1,
    created_date: new Date().getTime()     
  },
  {
    id: 3,
    author: "윤선영",
    content: "오늘 저녁은 뭐 먹지?",
    emotion: 4,
    created_date: new Date().getTime()     // 시간 객체 생성(현재 시간 기준).숫자로 시간(밀리second) 반환
  },
  {
    id: 4,
    author: "박지우",
    content: "뇽이 보고싶당",
    emotion: 5,
    created_date: new Date().getTime()     // 시간 객체 생성(현재 시간 기준).숫자로 시간(밀리second) 반환
  }
]

function App() {
  return (
    <div className="App">
      <DiaryEditor/>
      <DiaryList diaryList={dummyList}/>
    </div>
  );
}

export default App;
