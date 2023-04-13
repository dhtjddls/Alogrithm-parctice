function solution(numbers) {
  var answer = 0;
  // 배열에서
  for (let i = 0; i <= 9; i++) {
    if (numbers.indexOf(i) == -1) {
      answer += i;
    }
  }
  return answer;
}
