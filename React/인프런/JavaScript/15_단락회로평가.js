// 논리연산자 뒤에 위치한 피연산자를 확인할 필요 없이 연산이 끝나는 걸 보고 단락회로 평가라고 함!

// && 연산자 : 피연산자 두개가 다 true일 때만 true
console.log(true && true);
console.log(false && true); // 앞이 false면 뒤의 피연산자 확인할 필요X

// || 연산자 : 피연산자 둘 중 하나만 true여도 true 
console.log(true || false); // 앞이 true면 뒤의 피연산자 확인할 필요X

console.log(!true);

///////////////////////////////////////////////////////////////
// 논리연산자의 피연산자가 truthy나 falsy면 단락회로 평가를 멋있게 사용할 수 있다 -> 함수 사용!

const getName = (person) => {
    if (!person) {
        return "객체가 아닙니다.";
    }
    return person.name;
}

// getName함수에 단락 회로 평가를 사용한다면?
const getName2 = (person) => {
    // return person && person.name; -> 요렇게만 써주면 name2가 undefined를 반환함(person의 값을 그대로 반환)
    const name = person && person.name; // person이 undefined이므로 name은 undefined
    return name || "객체가 아닙니다.";  // 앞이 falsy면 뒤의 값 확인후 return함!
}

let person;
const name = getName(person);
console.log(name);  // 객체가 아닙니다.
const name2 = getName2(person);
console.log(name2)  // 객체가 아닙니다.
