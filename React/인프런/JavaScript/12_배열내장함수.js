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
