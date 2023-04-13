function solution(n) {
  var answer = "";
  let arr = String(n).split("");
  sortedArr = arr.sort((a, b) => b - a);
  sortedArr.forEach((element) => {
    answer += element;
  });
  return Number(answer);
}
