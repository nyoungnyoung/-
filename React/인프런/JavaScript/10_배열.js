// 배열 : 자바 스크립트의 자료형 중 Non-Primitive Type(비 원시 타입)에 해당
// 배열 생성 방법
// 1. 생성자 이용
let arr = new Array();

// 2. 배열 리터럴(대괄호) 사용 -> 이거 사용하기!
// 배열에도 객체와 동일하게 어떤 자료형이든 넣을 수 있음!!
let arr2 = [1, "2", true, undefined, {}, [], function () {}];

console.log(arr); // []
console.log(arr2); // [ 1, '2', true, undefined, {}, [], [Function (anonymous)] ]

///////////////////////////////////////////////////////////////

// 배열의 요소 각각에 접근해보기 -> 인덱스로 접근하면 됨!
let arr3 = [1, 2, 3, 4, 5];
console.log(arr3[0]); // 1
console.log(arr3[1]); // 2
console.log(arr3[2]); // 3
console.log(arr3[3]); // 4
console.log(arr3[4]); // 5
console.log(arr3[5]); // undefined

///////////////////////////////////////////////////////////////

// 배열에 요소 추가하기 -> push 메서드 사용.. 파이썬이랑 똑같네
arr3.push(6);
console.log(arr3); // [ 1, 2, 3, 4, 5, 6 ]

///////////////////////////////////////////////////////////////

// 배열의 길이 확인 -> length 메서드 사용
console.log(arr3.length); // 6
