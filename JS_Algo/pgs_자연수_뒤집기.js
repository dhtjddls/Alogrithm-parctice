function solution(n) {
  var answer = [];
  let arr = String(n).split("").reverse();
  arr.forEach((e) => {
    answer.push(Number(e));
  });
  return answer;
}
