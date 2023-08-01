/* 
  2. min(a, b) 함수 만들기
  -> a 와 b 중에서 더 작은 값을 반환해주는 함수 min(a, b)를 만들어 보세요!
  -> a == b인 경우엔 a나 b 중 어떤 것을 반환해도 상관없습니다. */

// (1) if 문을 활용해 만들기
function min(a, b) {
  //(코드를 완성해보세요!)

  if (a>b) {
    return b;
  }
  else {
    return a;
  }

}

// (2) ? 를 활용해 만들기
function min(a, b) {
  //(코드를 완성해보세요!)

  return (a>b) ? b : a;
}
let minimum = min(242, 555);
console.log(minimum);
