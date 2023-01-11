import "./App.css";
import Hello from "./component/Hello";
// import Welcome from "./component/Welcome";
// import styles from "./App.module.css";

function App() {
  // const name = "Tom";
  // const naver = {
  //   name: "네이버",
  //   url: "https://naver.com",
  // };
  return (
    <div className="App">
      {/* <h1
        style={{
          color: "red",
          backgroundColor: "yellow",
        }}
      >
        Hello, {name}, <p>{2 + 3}</p>
      </h1>
      <a href={naver.url}>{naver.name}</a> */}
      <Hello />
      {/* <Hello />
      <Hello />
      <div className={styles.box}>App</div>
      <Welcome /> */}
    </div>
  );
}

export default App;

// const user = {
//   name: "Jane",
// };
