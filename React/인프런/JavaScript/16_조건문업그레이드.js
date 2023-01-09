function isKoreanFood(food) {
    if(food === "불고기" || food === "비빔밥" || food === "떡볶이"){
        return true;
    }
    return false;
}

const food1 = isKoreanFood("불고기");
const food2 = isKoreanFood("파스타");
console.log(food1); // true
console.log(food2); // false

///////////////////////////////////////////////////////////////
// 이 조건에 들어갈 한식 종류가 많아지면 코드가 너무 길어지는 문제 -> 배열의 내장함수 includes 사용으로 해결 가능
function isKoreanFood2(food) {
    if(["불고기", "떡볶이", "비빔밥"].includes(food)) {
        return true;
    }
    return false;
}

const food3 = isKoreanFood2("불고기");
const food4 = isKoreanFood2("파스타");
console.log(food3); // true
console.log(food4); // false

///////////////////////////////////////////////////////////////
const getMeal = (mealType) => {
    if (mealType === "한식") return "불고기";
    if (mealType === "양식") return "파스타";
    if (mealType === "중식") return "멘보샤";
    if (mealType === "일식") return "초밥";
    return "굶기";
}

console.log(getMeal("한식"));   // 불고기
console.log(getMeal("중식"));   // 멘보샤
console.log(getMeal(""));       // 굶기

// 이 식사유형도 존재하는 모든 국가를 다 포함하려면 코드가 엄청 길어질 것 -> 객체의 프로퍼티에 접근하는 괄호표기법으로 해결 가능
const meal = {
    한식 : "불고기",
    중식 : "멘보샤",
    일식 : "초밥",
    양식 : "파스타",
    인도식 : "카레",
};

const getMeal2 = (mealType) => {
    return meal[mealType] || "굶기"
}

console.log(getMeal2("한식"));  // 불고기
console.log(getMeal2());        // 굶기