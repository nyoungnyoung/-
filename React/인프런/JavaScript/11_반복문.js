// 1. for 반복문(초기식; 조건식; 연산식)
for (let i = 1; i <= 10; i++) {
  // 반복 수행할 명령
  console.log("윤선영"); // 10번동안 내 이름 출력됨
}

///////////////////////////////////////////////////////////////

// 반복문으로 배열 순회하기
const arr = ["a", "b", "c"];
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

// 배열과 반복문 활용하여 객체 순회하기
let person = {
  name: "이정환",
  age: 25,
  tall: 175,
};

const personKeys = Object.keys(person); // 오브젝트.keys 함수에 객체 자체를 넣어주면
console.log(personKeys); // [ 'name', 'age', 'tall' ]

for (let i = 0; i < personKeys.length; i++) {
  // console.log(personKeys[i]);
  const curKey = personKeys[i];
  const curValue = person[curKey];
  console.log(`${curKey}:${curValue}`);
}
// name:이정환
// age:25
// tall:175

const personValues = Object.values(person);
for (let i = 0; i < personValues.length; i++) {
  console.log(personValues[i]);
}
// 이정환
// 25
// 175
