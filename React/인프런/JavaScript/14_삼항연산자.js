// 조건문을 파격적으로 줄여서 사용할 수 있는 문법!!

let a = 3;
if (a >= 0) {
    console.log("양수");
} else {
    console.log("음수");
}       // 양수

// 삼항연산자로 표현해보면 이렇게 된다!
// 조건식 ? 조건식이 참일 때 수행할 식 : 조건식이 거짓일 때 수행할 식
a >= 0 ? console.log("양수") : console.log("음수");     // 양수


let b = [];

if(b.length === 0){
    console.log("빈 배열입니다.")
} else {
    console.log("빈 배열이 아닙니다.")
}       // 빈 배열입니다.

// 삼항연산자
b.length === 0 ? console.log("빈 배열입니다.") : console.log("빈 배열이 아닙니다.");    // 빈 배열입니다.

const arrayStatus = b.length === 0 ? "빈 배열" : "안 빈 배열";  // 삼항연산자의 결과를 어떤 값에 저장해 사용 할 수 있음
console.log(arrayStatus);   // 빈 배열

///////////////////////////////////////////////////////////////

// 삼항연산자와 truthy, falsy값
let c;

const result = c ? true : false;
console.log(result);    // false

///////////////////////////////////////////////////////////////

// 삼항연산자의 중첩 -> 가독성이 떨어지는 편이기 때문에 if문 사용을 권장!
// 학점 계산 프로그램 : 90점이상 A+ 50점 이상 B+ 둘다 아니면 F

let score = 100;

score >= 90
    ? console.log("A+")
    : score >= 50
    ? console.log("B+")
    : console.log("F")

if (score >= 90) {
    console.log("A+")
} else if (score >= 50) {
    console.log("B+")
} else {
    console.log("F")
}