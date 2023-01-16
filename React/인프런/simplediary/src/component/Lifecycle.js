import React, { useEffect, useState } from "react";

const UnmountTest = () => {
  // 콜백함수가 함수를 하나 리턴하게 만들면 컴포넌트가 unmount되는 순간
  // (컴포넌트가 화면에서 사라지는 순간)을 제어할 수 있음!
  useEffect(() => {
    console.log("Mount!");
    return () => {
      // unmount 시점에 실행
      console.log("Unmount!");
    };
  }, []);
  return <div>Unmount Testing Component</div>;
};

const Lifecycle = () => {
  const [isVisible, setIsVisible] = useState(false);
  const toggle = () => setIsVisible(!isVisible);
  //   const [count, setCount] = useState(0);
  //   const [text, setText] = useState("");

  //   // 콜백함수 뒤에 전달하는 dependency array가 빈배열이면 컴포넌트가 탄생(Mount)하는 시점!
  //   // 아무리 버튼 클릭해도 Mount!는 한번만 콘솔에 찍힌다.
  //   useEffect(() => {
  //     console.log("Mount!");
  //   }, []);

  //   // dependency array를 전달하지 않으면 컴포넌트가 업데이트(Update) 되는 순간
  //   // state가 바뀌거나, props가 바뀌거나, 부모 컴포넌트가 리렌더링되는 순간을 말함
  //   useEffect(() => {
  //     console.log("Update!");
  //   });

  //   // dependency array에 값을 전달한다면 이 값이 변화할 때 콜백함수 수행됨
  //   // dependency array를 잘 활용하면 우리가 감지하고 싶은 값이 변화하는 순간에만 콜백함수 실행시켜줄 수 있음!!
  //   useEffect(() => {
  //     console.log(`count is update : ${count}`);
  //     if (count > 5) {
  //       alert("count가 5를 넘었습니다. 따라서 1로 초기화합니다.");
  //       setCount(1);
  //     }
  //   }, [count]);

  //   useEffect(() => {
  //     console.log(`text is update : ${text}`);
  //   }, [text]);

  return (
    <div style={{ padding: 20 }}>
      {/* {count}
      <button onClick={() => setCount(count + 1)}>+</button>
      <div>
        <input value={text} onChange={(e) => setText(e.target.value)} />
      </div> */}
      <button onClick={toggle}>ON/OFF</button>
      {isVisible && <UnmountTest />}
      {/* isVisible이 true면 unmountTest를 반환! */}
    </div>
  );
};

export default Lifecycle;
