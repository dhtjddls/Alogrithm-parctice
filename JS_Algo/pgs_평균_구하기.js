function solution(arr) {
  var answer = 0;
  answer = arr.reduce((p, c) => p + c, 0) / arr.length;
  return answer;
}
