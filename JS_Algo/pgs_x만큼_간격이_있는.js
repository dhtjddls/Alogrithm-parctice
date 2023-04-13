// n만큼 반복
function solution(x, n) {
  var answer = [];
  let cnt = 0;
  for (let i = 0; i < n; i++) {
    cnt += x;
    answer.push(cnt);
  }
  return answer;
}
