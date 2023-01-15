// // 01_ hello_world
// console.log("hello world");


// // 02_변수와상수
// // 변수명에는 기호 사용할 수 없음! '_', '$'는 가능
// // 변수명은 반드시 영어로 시작해야함
// // 예약어는 변수명으로 사용할 수 없음
// // let 대신 var도 사용 가능하지만 let만 사용하는 것을 추천
// let age = 25;
// console.log(age); // 25
// age = 30;
// console.log(age); // 30
// // 상수는 변하지 않는 수로, const로 선언 가능
// // const로 선언한 내용은 재할당 불가능함!
// const msg = "hi";
// console.log(msg);


// // 03_자료형과형변환
// let age = 25;   // 정수
// let tall = 175.9;   // 실수
// let inf = Infinity;
// let minusInf = -Infinity;
// let nan = NaN;

// let name = "winterlood";
// let name2 = "이정환";
// let name3 = `winterlood ${name2}`;    // template literal

// let isSwitchOff = true;

// let a = null;

// let variable;   // undefined

// let numberA = 12;
// let numberB = "2";
// console.log(numberA * numberB)    // 24 : 묵시적형변환
// console.log(numberA + numberB)    // 122 : 
// console.log(numberA + parseInt(numberB));   // 14 : 명시적형변환


// // 04_연산자
// // 대입연산자 =
// let a = 1;
// let b = 2;
// let c = "2";

// // 산술연산자 +*-/%
// console.log(a + b);
// console.log(a * b);
// console.log(a - b);
// console.log(a / b);
// console.log(a % b);

// // 연결연산자 + : 문자열끼리 연결해주는 연산자
// console.log(a + c);

// // 복합연산자 += *= -= /= %=
// a += 10;
// console.log(a)    // 11

// // 증감연산자 ++ -- : 숫자형에만 사용 가능
// // 증감연산자는 변수 뒤에 쓰면 해당 라인이 끝난 뒤에 값이 변동됨(후위연산)
// // 변수 앞에 쓰면 해당 라인에도 값이 변동됨(전위연산)
// a++;        
// console.log(a)    // 12
// console.log(a++)  // 12
// console.log(++a)  // 13

// // 논리연산자 ! && || : boolean 자료형을 위한 연산자
// console.log(!false)         // true
// console.log(true && true)   // true : 피연산자 둘다 참일때만 참
// console.log(true || false)  // true : 피연산자 줄 중 하나만 참이면 참

// // 비교연산자 == != 값만 비교 === !== 타입까지 비교(주로 이거 사용) < > <= >= 
// let compareA = 1 == "1";
// console.log(compareA);

// // typeof 연산자
// console.log(typeof compareA);

// // null변환 연산자 ?? : 피연산자 중 null이나 undefined가 아닌 값 선택
// let a;
// a = a ?? 10;
// console.log(a);   // 10


// 05_조건문
// if문
let a = 5;

if (a >= 7) {
    console.log("7 이상입니다");
} else if (a >= 5) {
    console.log("5 이상입니다.");
} else {
    console.log("5 미만입니다.");
}

let country = "ko";

if (country === "ko") {
    console.log("한국");
} else if (country === "cn") {
    console.log("중국");
} else {
    console.log("미분류");
}

// switch문
switch (country) {
    case "ko":
        console.log("한국");
        break;
    case "cn":
        console.log("중국");
        break;
    case "jp":
        console.log("일본");
        break;
    case "uk":
        console.log("중국");
        break;
    default:
        console.log("미분류");
        break;
}