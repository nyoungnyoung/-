// 자바스크립트의 코드 실행과 굉장히 큰 연관이 있음!!
function taskA() {
  // 자바스크립트 내 setTimeout이라는 타이머를 만들 수 있는 내장 비동기함수 있음
  // 파라미터로 콜백함수와 delay time(ms단위) 넣어주면 된다! 1000ms = 1초
  setTimeout(() => {
    console.log("A TASK END");
  }, 2000);
}

function taskB(a, b, callback) {
  setTimeout(() => {
    const res = a + b;
    callback(res);
  }, 3000);
}

function taskC(a, callback) {
  setTimeout(() => {
    const res = a * 2;
    callback(res);
  }, 1000);
}

function taskD(a, callback) {
  setTimeout(() => {
    const res = a * -1;
    callback(res);
  }, 2000);
}

taskA();
console.log("A 코드 끝"); // 코드 끝이 먼저 출력된 후 A TASK END 출력됨!(비동기 방식)
taskB(3, 4, (res) => {
  console.log("B TASK RESULT :", res);
});
console.log("B 코드 끝");
taskC(7, (res) => {
  console.log("C TASK RESULT :", res);
});
console.log("C 코드 끝");
taskD(14, (res) => {
  console.log("D TASK RESULT :", res);
});
console.log("D 코드 끝");

///////////////////////////////////////////////////////////////

// 호출을 좀 다르게 해보자
// -> 비동기 처리의 결과를 또 다른 비동기 처리의 값으로 전달할 수 있음
// 이렇게 콜백함수를 계속 연달아 쓰다보면 콜백지옥이 된다...
taskB(4, 5, (b_res) => {
  console.log("B 두번째 결과 :", b_res);
  taskC(b_res, (c_res) => {
    console.log("C 두번째 결과 :", c_res);
    taskD(c_res, (d_res) => {
      console.log("D 두번째 결과 :", d_res);
    });
  });
});
