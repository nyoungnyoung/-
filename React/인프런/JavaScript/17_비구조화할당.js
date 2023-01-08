// 배열과 객체를 우아하게 사용하는 방법
// 배열이나 객체에서 원하는 값을 빠르게 뽑아내는 방법
let arr = ["one", "two", "three"];

// let one = arr[0];
// let two = arr[1];
// let three = arr[2];

// console.log(one, two, three);   // one two three

///////////////////////////////////////////////////////////////

// 비구조화 할당을 이용해 한 줄 만에 변수에 0, 1, 2번 인덱스에 할당해 보기 -> 배열의 기본변수 비구조화 할당
let [one1, two1, three1] = arr; // arr이라는 배열의 0, 1, 2번 인덱스를 각각의 변수에 할당하라는 뜻
console.log(one1, two1, three1) // one two three

///////////////////////////////////////////////////////////////

// 더 간단하게! -> 배열의 선언분리 비 구조화 할당(할당 받지 못하는 변수는 undefined가 됨)
let [one2, two2, three2, four2] = ["one", "two", "three"];
console.log(one2, two2, three2, four2); // one two three undefined

// =""을 통해 할당 받지 못하는 경우의 기본값 지정가능)
let [one3, two3, three3, four3="four"] = ["one", "two", "three"];
console.log(one3, two3, three3, four3); // one two three four

///////////////////////////////////////////////////////////////

// 배열의 비구조화 할당을 이용하면 두 개의 변수를 서로 바꾸는 swap도 가능하다!
let a = 10;
let b = 20;
let tmp = 0;

// 원래 스왑하는 방법
tmp = a;
a = b;
b= tmp;
console.log(a, b);  // 20 10

// 비구조화할당 이용 스왑하기
[a, b] = [b, a];
console.log(a, b);  // 10 20

///////////////////////////////////////////////////////////////

// 객체의 비구조화 할당 -> 리액트 할 때 많이 사용하니까 꼭 기억해두기!!
let object = { one: "1", two: "2", three: "3" };

// 원래 객체의 프로퍼티를 각각의 변수에 할당하려면
// let one4 = object.one;
// let two4 = object.two;
// let three4 = object.three;
// console.log(one4, two4, three4) // 1 2 3

// 객체의 비구조화 할당 이용한다면? -> 'key'값을 기준으로 변수와 같은 키값을 갖는 프로퍼티의 value값을 변수에 저장(순서와 상관X)
let { one, two, three } = object;
console.log(one, two, three)    // 1 2 3

// 근데 다른 변수 이름을 쓰고 싶은데요??ㅜㅜ 기본값도 설정하고 싶은데요?
let { one:one5, two:two5, three:three5, abc="abc" } = object;
console.log(one5, two5, three5, abc);   // 1 2 3 abc