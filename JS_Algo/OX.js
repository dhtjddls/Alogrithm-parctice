function addNum(num) {
  cnt = 0;
  for (let i = 1; i <= num; i++) cnt += i;
  return cnt;
}

function solution(str) {
  let answer = 0;
  console.log(str.split("X"));

  for (i of str.split("X")) {
    answer += addNum(i.length);
  }
  return answer;
}
let str = "OXOOOXXXOXOOXOOOOOXO";
console.log(solution(str));
