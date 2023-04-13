function solution(array, commands) {
  let answer = [];
  for (items of commands) {
    let start = items[0] - 1;
    let end = items[1];
    let k = items[2] - 1;
    answer.push(array.slice(start, end).sort((a, b) => a - b)[k]);
  }
  return answer;
}
