let a = "string";

if(a){
    console.log("TRUE")
} else {
    console.log("FALSE")
}

// JavaScript의 Falsy : undefined, null, 0, -0, NaN, false, '', ""
// Truthy : '0', 'false', [], {}, function(){} 빈함수 -> 파이썬이랑 다르니까 주의!!

const getName = (person) => {
    if(!person){                    // false NOT => True
        return "객체가 아닙니다";
    }
    return person.name;
};

// 정상적인 상황
// let person = { name: "이정환" };
// const name = getName(person);
// console.log(name);  // 이정환

// person이 정의되어있지 않은(undefined) 상황이면? -> 오류 뜸! -> getName함수 내에서 if문 사용해서 걸러주기
let person;
const name = getName(person);
console.log(name);  // 이정환
