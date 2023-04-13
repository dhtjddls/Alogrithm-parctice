function solution(arr1, arr2) {
  let n = arr1.length;
  let m = arr1[0].length;
  answer = [];
  for (let i = 0; i < n; i++) {
    var arr = [];
    //
    for (let j = 0; j < m; j++) {
      arr.push(arr1[i][j] + arr2[i][j]);
    }
    answer.push(arr);
  }
  return answer;
}
