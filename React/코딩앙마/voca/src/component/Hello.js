// import World from "./World";
// import "./Hello.css";
// import styles from "./Hello.module.css";

// const Hello = function () {
//   function showName() {
//     console.log("Mike");
//   }
//   function showAge(age) {
//     console.log(age);
//   }
//   // function showText(e) {
//   //   console.log(e.target.value);
//   // }
//   // function showText(txt) {
//   //   console.log(txt);
//   // }
//   return (
//     <div>
//       <h1
//       // style={{
//       //   color: "#f00",
//       //   borderRight: "2px soloid #000",
//       //   marginBottom: "30px",
//       //   opacity: 0.5,
//       // }}
//       >
//         Hello
//       </h1>
//       <button onClick={showName}>Show name</button>
//       <button
//         onClick={() => {
//           // console.log(30);
//           showAge(10);
//         }}
//       >
//         Show age
//       </button>
//       {/* <input type="text" onChange={showText}/> */}
//       <input
//         type="text"
//         onChange={(e) => {
//           console.log(e.target.value);
//         }}
//       />
//       {/* <input
//         type="text"
//         onChange={(e) => {
//           const txt = e.target.value;
//           showText(txt);
//         }}
//       /> */}
//       {/* <div className={styles.box}>Hello</div>
//       <World />
//       <World /> */}
//     </div>
//   );
// };

// 화살표 함수 사용시
// const Hello = () => {
//   return <h1>Hello</h1>;
// };
import { useState } from "react";
import UserName from "./UserName";

// export default function Hello(props) {
export default function Hello({ age }) {
  // let name = "Mike";
  // console.log(props);
  const [name, setName] = useState("Mike");
  const msg = age > 19 ? "성인입니다." : "미성년자입니다.";
  // const [age, setAge] = useState(props.age);

  // function changeName() {
  //   // name = name === "Mike" ? "Jane" : "Mike";
  //   // console.log(name);
  //   // document.getElementById("name").innerText = name;

  //   // 이렇게도 작성 가능
  //   // setName(name === "Mike" ? "Jane" : "Mike");
  //   const newName = name === "Mike" ? "Jane" : "Mike";
  //   setName(newName);
  // }

  return (
    <div>
      {/* <h1>state</h1> */}
      <h2>
        {/* {name}({props.age}) */}
        {name}({age}) : {msg}
      </h2>
      {/* 이렇게도 작성 가능
      <button onClick={changeName}>Change</button> */}
      <UserName name={name} />
      <button
        onClick={() => {
          setName(name === "Mike" ? "Jane" : "Mike");
          // setAge(age + 1);
        }}
      >
        Change
      </button>
    </div>
  );
}

// 아래처럼 사용해도 괜찮음!!
// export default function Hello() {
//   return <h1>Hello</h1>;
// }
