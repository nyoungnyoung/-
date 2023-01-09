// spread 연산자(...) : 배열과 객체를 한 줄로 펼치는 방법 
const cookie = {
    base: "cookie",
    madeIn: "korea",
};

const chocochipCookie = {
    // base: "cookie",
    // madIn: "korea",
    ...cookie,
    toping: "chocochip",
}

const blueberryCookie = {
    // base: "cookie",
    // madeIn: "korea",
    ...cookie,
    toping: "blueberry",
}

const strawberryCookie = {
    // base: "cookie",
    // madeIn: "korea",
    ...cookie,
    toping: "strawberry",
}

console.log(chocochipCookie)    // { base: 'cookie', madeIn: 'korea', toping: 'chocochip' }
console.log(blueberryCookie)    // { base: 'cookie', madeIn: 'korea', toping: 'blueberry' }
console.log(strawberryCookie)   // { base: 'cookie', madeIn: 'korea', toping: 'strawberry' }

///////////////////////////////////////////////////////////////

// 배열에 spread 연산자 사용하기
const noTopingCookies = ["촉촉한쿠키", "안촉촉한쿠키"];
const topingCookies = ["바나나쿠키", "블루베리쿠키", "딸기쿠키", "초코칩쿠키"];

const allCookies = [...noTopingCookies, "함정쿠키", ...topingCookies];  // concat연산자와 다른점!
console.log(allCookies);    // [ '촉촉한쿠키', '안촉촉한쿠키', '함정쿠키', '바나나쿠키', '블루베리쿠키', '딸기쿠키', '초코칩쿠키' ]