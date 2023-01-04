// 객체 : 자바 스크립트의 자료형 중 Non-Primitive Type(비 원시 타입)에 해당
// 객체 생성 방법
// 1. 객체 생성자를 활용해 생성
let person = new Object();

// 2. 객체 리터럴 방식(중괄호) -> 앞으로는 이런 방식으로! 위에껀 귀찮으니까...
let person2 = {
  key: "value", // 프로퍼티 (객체 프로퍼티), 객체 속성, 객체가 갖고있는 데이터라고 생각하면 됨
  key1: true, // 프로퍼티의 value에는 어떤 자료형이 와도 상관X!
  key2: undefined,
  key3: [1, 2],
  key4: function () {},
};

console.log(person2); // { key: 'value', key1: true, key2: undefined, key3: [ 1, 2 ], key4: [Function: key4] }

///////////////////////////////////////////////////////////////

// 객체의 프로퍼티를 꺼내서 사용하는 방법 : 표기법
// 1) 점표기법! 없는 프로퍼티에 접근하려하면 undefined가 나옴
console.log(person2.key1); // true
console.log(person2.key3); // [ 1, 2 ]

// 2) 괄호 표기법 -> 함수 등에서 동적인 파라미터를 전달받는 상황에 사용하면 좋음!
console.log(person2["key3"]); // [ 1, 2 ]
console.log(getPropertyValue("key1")); // true (호이스팅)

function getPropertyValue(key) {
  return person2[key];
}

///////////////////////////////////////////////////////////////

// 객체 생성 이후 프로퍼티 추가, 삭제 방법
// 이 때는 let 대신 const도 사용 가능함 -> person3이라는 상수가 갖는
// 객체를 수정하는거지 person3 자체를 수정하는 게 아니기 때문
let person3 = {
  name: "이정환", // 객체의 '멤버'라고 부름
  age: 25,
  say: function () {
    console.log(`안녕 나는 ${this.name}`);
    console.log(`안녕 나는 ${this["name"]}`);
  }, // 객체 안에 들어있는 함수 -> 객체의 '메서드'라고 부름
};

person3.location = "한국";
person3["gender"] = "남성";
person3.name = "이정환 A";
person3["age"] = 28;
console.log(person3); // { name: '이정환 A', age: 28, location: '한국', gender: '남성' }

// 프로퍼티 삭제
// 1) delete 사용
delete person3.age;
delete person3["gender"];
console.log(person3); // { name: '이정환 A', say: [Function: say], location: '한국' }
// 2) null 사용 -> 추천
person3.location = null;
console.log(person3); // { name: '이정환 A', say: [Function: say], location: null }

// 객체의 value값이 함수일때 표기법으로 접근하여 함수 호출 가능
person3.say(); // 안녕 나는 이정환
person3["say"]; // 안녕 나는 이정환

///////////////////////////////////////////////////////////////

// 존재하지 않는 프로퍼티에 접근하려 할 때
console.log(person3.gender); // undefined -> 존재하지 않는데도 접근은 가능함...

// 해당 프로퍼티가 존재하는지 안하는지 확인하려면? in 연산자 활용!!
console.log(`name : ${"name" in person3}`); // name : true
console.log(`age : ${"age" in person3}`); // age : false
