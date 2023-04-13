function solution(arr, divisor) {
  var answer = [];
  let result = arr.filter((e) => e % divisor == 0).sort((a, b) => a - b);
  answer = result;
  if (result.length < 1) {
    answer.push(-1);
  }
  return answer;
}
