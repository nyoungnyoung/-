import { useContext } from "react";
import { DiaryStateContext } from "../App";
import DiaryItem from "./DiaryItem";

const DiaryList = () => {
  const diaryList = useContext(DiaryStateContext);
  // console.log(diaryList)
  return (
    <div className="DiaryList">
      <h2>일기 리스트</h2>
      <h4>{diaryList.length}개의 일기가 있습니다.</h4>
      <div>
        {/* map의 파라미터로 it.idx 사용해 주어도 문제는 생기지 않지만,
                배열의 값을 수정, 삭제, 업데이트 하면서 배열의 순서가
                바뀌게 되면 문제가 생기기 때문에 고유한 값인 id를 이용하는 게 현명 */}
        {diaryList.map((it) => (
          // DairyList는 App에서 onDelete를 내려받고, 이걸 또 DiaryItem으로 내려줘야함
          <DiaryItem key={it.id} {...it} />
        ))}
      </div>
    </div>
  );
};

// 빈배열이 전달되었을 때 에러 뜨지 않도록 default값 설정해주기
DiaryList.defaultProps = {
  diaryList: [],
};

export default DiaryList;
