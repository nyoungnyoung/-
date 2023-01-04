// 3. 콜백함수 -> 다른 함수의 매개변수로 함수를 넘겨 준 것을 의미함!
// 콜백함수를 이해하기 위해 기분에 따라 다른 동작을 하게 하는 함수를 만들어보자

// 기분을 체크하는 함수 -> 함수 선언식으로 구현
function checkMood(mood) {
  if (mood === "good") {
    // 기분 좋을 때 하는 동작
    sing();
  } else {
    // 기분 안좋을 때 하는 동작
    cry();
  }
}

// 우는 동작
function cry() {
  console.log("ACTION :: CRY");
}

// 노래하는 동작
function sing() {
  console.log("ACTION :: SING");
}

// 춤추는 동작
function dance() {
  console.log("ACTION :: DANCE");
}

checkMood("good");
checkMood("sad");

///////////////////////////////////////////////////////////////

// 콜백함수로 구현해보기
// checkMood2라는 함수의 goodCallback, badCallback라는 매개변수로
// sing, cry라는 함수가 값으로 들어온 것! 함수를 값에 담는 것 -> 함수 표현식
function checkMood2(mood, goodCallback, badCallback) {
  if (mood === "good") {
    goodCallback();
  } else {
    badCallback();
  }
}

checkMood2("sad", sing, cry);
