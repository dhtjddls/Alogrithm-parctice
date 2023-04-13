function solution(arr) {
  result = [];
  for (let i = 1; i < arr.length + 1; i++) {
    if (arr[i] != arr[i - 1]) {
      result.push(arr[i - 1]);
    }
  }
  return result;
}
