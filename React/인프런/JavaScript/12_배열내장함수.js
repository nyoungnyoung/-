// for문 사용 배열 순회
const arr = [1, 2, 3, 4];
const newArr = [];
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

// 배열 순회 내장함수 forEach

// 콜백함수 형태와 동일한 기능! 하나하나의 요소를 forEach
// 메서드 안에 전달되는 콜백함수에 파라미터로 한번씩 전달
// arr.forEach(function(elm){
//     console.log(elm * 2);
// })

arr.forEach((elm) => console.log(elm));

///////////////////////////////////////////////////////////////

// 새로운 배열에 배열의 각 요소 * 2한 값을 넣기
arr.forEach(function (elm) {
  newArr.push(elm * 2);
});

// 내장함수 map -> 위의 작업을 더 간편하게 할 수 있게 해 주는 내장함수
// 똑같이 콜백함수를 전달하는데, 맵이라는 내장함수는
// 콜백함수에서 return을 할 수 있음!
const newArr2 = arr.map((elm) => {
  return elm * 2;
});

console.log(newArr2); // [ 2, 4, 6, 8 ]

///////////////////////////////////////////////////////////////

// 어떤 숫자가 배열 안에 존재하면 true를 출력하게 만들기
let number = 3;
arr.forEach((elm) => {
  if (elm === number) {
    console.log(true); // true
  }
});

// 내장함수 includes
console.log(arr.includes(number)); // true

///////////////////////////////////////////////////////////////

// 내장함수 indexOf -> 어떤 인자가 배열안에, 몇번째 인덱스에 존재하는지 찾아주는 역할
console.log(arr.indexOf(number)); // 2
console.log(arr.indexOf("3")); // -1 : 배열안에 해당 값이 존재하지 않을 때

///////////////////////////////////////////////////////////////

// 단순한 배열이 아니라, 복잡한 객체들로 이루어진 배열이라면 includes나
// indexOf를 사용하기에는 어려움이 있음! 그러면 이런 객체배열에서 원하는
// 속성을 갖는 (ex.색상이 green인) 배열 요소의 인덱스를 찾으려면?
// findIndex 배열 내장함수(메서드) -> 파라미터 안에는 콜백함수를 보내줌
// 이 콜백함수는 각각의 요소들에 모두 순회를 하면서 사용
// 콜백함수를 전달해서, 콜백함수가 true를 반환하는 첫번째 요소의 index 반환
const arr2 = [
  { color: "red" },
  { color: "black" },
  { color: "blue" },
  { color: "green" },
  { color: "blue" },
];

let num = 3;

console.log(arr2.findIndex((elm) => elm.color === "green")); // 3
console.log(arr2.findIndex((elm) => elm.color === "red")); // 0
// 위 코드와 동일한 화살표함수의 기본형
console.log(
  arr.findIndex((elm) => {
    return elm.color === "red";
  })
);

// 주의점 : findIndex함수는 조건과 일치하는 요소가 여러개 있을 때
// 가장 먼저 만나는 요소를 반환할 수 밖에 없음!
console.log(arr2.findIndex((elm) => elm.color === "blue")); // 2

///////////////////////////////////////////////////////////////

// findIndex를 통해 우리가 알 수 있는건 결국 인덱스이므로, 그 요소에 직접
// 접근하기 위해서는 이 인덱스를 활용해주어야함
const idx = arr2.findIndex((elm) => elm.color === "blue");
console.log(arr2[idx]); // { color: 'blue' }

// find 메서드 -> 인덱스를 가져오는 것이 아니라 조건에 일치하는 첫번째 요소를 가져옴
const element = arr2.find((elm) => {
  return elm.color === "blue";
});

console.log(element); // { color: 'blue' }

///////////////////////////////////////////////////////////////

// filter 메서드
// 매개변수로 전달한 콜백함수가 true를 반환하는 모든 요소를 배열로 반환
const arr3 = [
  { num: 1, color: "red" },
  { num: 2, color: "black" },
  { num: 3, color: "blue" },
  { num: 4, color: "green" },
  { num: 5, color: "blue" },
];

console.log(arr3.filter((elm) => elm.color === "blue")); // [ { num: 3, color: 'blue' }, { num: 5, color: 'blue' } ]

///////////////////////////////////////////////////////////////

// slice 메서드 -> 두개의 파라미터(begin, end) 존재함!
// begin부터 end-1번째 인덱스까지 slice해서 반환함!

// 파라미터로 아무것도 전달하지 않을 경우 -> 아무일도 발생X
console.log(arr3.slice());
// [
//     { num: 1, color: 'red' },
//     { num: 2, color: 'black' },
//     { num: 3, color: 'blue' },
//     { num: 4, color: 'green' },
//     { num: 5, color: 'blue' }
// ]

console.log(arr3.slice(0, 2));
// [ { num: 1, color: 'red' }, { num: 2, color: 'black' } ]

///////////////////////////////////////////////////////////////

// concat 내장함수 -> 배열 두개를 붙이고 싶을 때 사용!
// 매개변수로 받은 배열이 앞의 배열 뒤쪽에 붙은 형태로 return

const lst = [
  { num: 1, color: "red" },
  { num: 2, color: "black" },
  { num: 3, color: "blue" },
];

const lst2 = [
  { num: 4, color: "green" },
  { num: 5, color: "blue" },
];

console.log(lst.concat(lst2));

///////////////////////////////////////////////////////////////

// 배열 정렬
const chars = ["나", "다", "가"];
const nums = [0, 1, 3, 2, 10, 30, 20];

// sort 내장함수 -> 원본 배열을 사전순으로 정렬
chars.sort();
console.log(chars); // [ '가', '나', '다' ]

nums.sort();
console.log(nums); // [ 0, 1, 10, 2, 20, 3, 30 ]
// sort 내장함수는 문자열을 기준으로 정렬하기 때문에 이런 결과가 나옴
// 이렇게 숫자 배열을 sort를 이용해서 정렬하고 싶다면 sort 메서드의 인자로
// 비교함수를 만들어 넣어줘야 한다!

const compare = (a, b) => {
  // 크다 : a가 b보다 더 뒤에 있어야 한다
  if (a > b) {
    return 1;
  }
  // 작다 : a가 b보다 더 앞에 있어야 한다
  if (a < b) {
    return -1;
  }
  // 같다
  return 0;
};

nums.sort(compare);
console.log(nums); // [ 0, 1, 2, 3, 10, 20, 30 ]

///////////////////////////////////////////////////////////////

// join 내장함수 -> 배열의 모든 요소들을 문자열 형태로 합치는 함수

const arr4 = ["이정환", "님", "안녕하세요", "나오셨군요"];

console.log(arr4.join()); // 이정환,님,안녕하세요,나오셨군요
console.log(arr4.join(" ")); // 이정환 님 안녕하세요 나오셨군요
