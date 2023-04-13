function solution(N, arr1) {
  let answer = [];
  for (let i = 0; i < N + 2; i++) {
    answer.push(new Array(N + 2).fill(0));
  }

  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr1[i].length; j++) {
      if (arr1[i][j] === ".") continue;
      answer[i][j] += Number(arr1[i][j]);
      answer[i][j + 1] += Number(arr1[i][j]);
      answer[i][j + 2] += Number(arr1[i][j]);
      answer[i + 1][j + 2] += Number(arr1[i][j]);
      answer[i + 1][j] += Number(arr1[i][j]);
      answer[i + 2][j] += Number(arr1[i][j]);
      answer[i + 2][j + 1] += Number(arr1[i][j]);
      answer[i + 2][j + 2] += Number(arr1[i][j]);
    }
  }

  answer.pop();
  answer.shift();
  for (let i = 0; i < answer.length; i++) {
    answer[i].pop();
    answer[i].shift();
  }

  for (let i = 0; i < answer.length; i++) {
    for (let j = 0; j < answer[i].length; j++) {
      if (answer[i][j] >= 10) answer[i][j] = "M";
    }
  }

  return answer;
}

let N = 5;
let arr1 = [
  ["1", ".", ".", ".", "."],
  [".", ".", "3", ".", "."],
  [".", ".", ".", ".", "."],
  [".", "4", ".", ".", "."],
  [".", ".", ".", "9", "."],
];
console.log(solution(N, arr1));
