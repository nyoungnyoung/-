import React, { useContext, useEffect, useRef, useState } from "react";
import { DiaryDispatchContext } from "../App";

const DiaryItem = ({ author, content, created_date, emotion, id }) => {
  const { onRemove, onEdit } = useContext(DiaryDispatchContext);
  // useEffect(() => {
  //   console.log(`${id}번째 아이템 렌더!`);
  // });

  // 현재 수정중인지 아닌지 확인해 줄 state 만들어주기 -> true라면 JSX가 수정중인 페이지를 렌더링 해줘야함!
  const [isEdit, setIsEdit] = useState(false);
  const toggleIsEdit = () => setIsEdit(!isEdit); // 실행되면 원래 isEdit이 갖고 있던 값을 반전시킴

  // 수정 textarea에 입력되는 값 state로 관리
  const [localContent, setLocalContent] = useState(content);

  // 수정 시 데이터 검증 후 focus 해 주기 위한 변수 선언
  const localContentInput = useRef();

  // 코드의 가독성을 위해 onClick 이벤트 시 실행시켜줄 함수를 밖으로 빼주었음
  const handleRemove = () => {
    // console.log(id);
    if (window.confirm(`${id + 1}번째 일기를 정말 삭제하겠습니까?`)) {
      onRemove(id);
    }
  };

  // 수정 취소 눌렀을 때 input에 입력된 값 reset 해 주는 함수 필요
  const handleQuitEdit = () => {
    setIsEdit(false);
    setLocalContent(content);
  };

  // 수정완료 눌렀을 때 이벤트 처리해줄 함수
  const handleEdit = () => {
    if (localContent.length < 5) {
      localContentInput.current.focus();
      return;
    }
    if (window.confirm(`${id + 1}번째 일기를 수정하시겠습니까?`)) {
      onEdit(id, localContent);
      toggleIsEdit();
    }
  };

  return (
    <div className="DiaryItem">
      <div className="info">
        <span className="author_info">
          작성자 : {author} | 감정점수 : {emotion}
        </span>
        <br />
        <span className="date">{new Date(created_date).toLocaleString()}</span>
      </div>
      <div className="content">
        {isEdit ? (
          <div>
            <textarea
              ref={localContentInput}
              value={localContent}
              onChange={(e) => setLocalContent(e.target.value)}
            />
          </div>
        ) : (
          <div>{content}</div>
        )}
      </div>
      {isEdit ? (
        <div>
          <button onClick={handleQuitEdit}>수정취소</button>
          <button onClick={handleEdit}>수정완료</button>
        </div>
      ) : (
        <div>
          <button onClick={handleRemove}>삭제</button>
          <button onClick={toggleIsEdit}>수정</button>
        </div>
      )}
    </div>
  );
};

export default React.memo(DiaryItem);
