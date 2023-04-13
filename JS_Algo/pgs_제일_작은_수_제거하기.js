function solution(arr) {
  let minIdx = arr.indexOf(Math.min(...arr));
  arr.splice(minIdx, 1);
  if (arr.length < 1) arr.push(-1);
  return arr;
}
