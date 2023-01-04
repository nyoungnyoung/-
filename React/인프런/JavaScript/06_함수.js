// Ctrl + Alt + N -> 코드 실행

let width1 = 10;
let heigt1 = 20;
let area1 = width1 * heigt1;
console.log(area1);

let width2 = 30;
let heigt2 = 15;
let area2 = width2 * heigt2;
console.log(area2);

// 이렇게 반복적인 계산을 해야할 때, 함수를 사용하면 됨!

// 1. 함수 선언식 -> 함수 선언 방식의 함수 생성
function getArea() {
  let width = 10;
  let height = 20;
  let area = width * height;
  console.log(area);
}

getArea(); // 함수 호출! getArea라는 함수가 실행됨
console.log("getArea1함수 실행 완료");

// 함수에 매개변수를 전달해주고 싶을 경우 함수명 뒤에 오는 소괄호 내에 적어주면 됨!
function getArea2(width, height) {
  let area = width * height;
  // console.log(area)
  return area; // 함수로 계산한 값을 어떤 변수에 할당해 사용하고 싶다면 반환값 return 사용!
}

let square1 = getArea2(1, 200);
let square2 = getArea2(2, 200);
let square3 = getArea2(3, 200);
console.log("square1 :", square1);
console.log("getArea2함수 실행 완료");
// 함수 내부에 선언된 변수(지역변수, local)는 함수 외부에서 접근할 수 없다!
// 함수 외부에 선언된 변수(전역변수, global)는 함수 내부에서도 접근할 수 있다!
