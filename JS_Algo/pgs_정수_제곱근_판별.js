function solution(n) {
  var answer = 0;
  let x = Math.sqrt(n);
  Number.isInteger(x) ? (answer = Math.pow(x + 1, 2)) : (answer = -1);
  return answer;
}
