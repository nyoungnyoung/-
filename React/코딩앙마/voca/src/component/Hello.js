// import World from "./World";
// import "./Hello.css";
// import styles from "./Hello.module.css";

const Hello = function () {
  function showName() {
    console.log("Mike");
  }
  function showAge(age) {
    console.log(age);
  }
  // function showText(e) {
  //   console.log(e.target.value);
  // }
  // function showText(txt) {
  //   console.log(txt);
  // }
  return (
    <div>
      <h1
      // style={{
      //   color: "#f00",
      //   borderRight: "2px soloid #000",
      //   marginBottom: "30px",
      //   opacity: 0.5,
      // }}
      >
        Hello
      </h1>
      <button onClick={showName}>Show name</button>
      <button
        onClick={() => {
          // console.log(30);
          showAge(10);
        }}
      >
        Show age
      </button>
      {/* <input type="text" onChange={showText}/> */}
      <input type="text" onChange={(e) => {
        console.log(e.target.value)
      }} />
      {/* <input
        type="text"
        onChange={(e) => {
          const txt = e.target.value;
          showText(txt);
        }}
      /> */}
      {/* <div className={styles.box}>Hello</div>
      <World />
      <World /> */}
    </div>
  );
};

// 화살표 함수 사용시
// const Hello = () => {
//   return <h1>Hello</h1>;
// };

export default Hello;

// 아래처럼 사용해도 괜찮음!!
// export default function Hello() {
//   return <h1>Hello</h1>;
// }
