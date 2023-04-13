function solution(num) {
  let cash = 1000 - num;
  let answer = 0;
  while (cash !== 0) {
    if (cash / 500 > 1) {
      answer += Math.floor(cash / 500);
      cash %= 500;
    } else if (cash / 100 > 1) {
      answer += Math.floor(cash / 100);
      cash %= 100;
    } else if (cash / 50 > 1) {
      answer += Math.floor(cash / 50);
      cash %= 50;
    } else {
      answer += Math.floor(cash / 10);
      cash %= 10;
    }
  }
  return answer;
}
let num1 = 160;
console.log(solution(num1));
