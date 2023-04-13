function solution(n) {
  s = String(n);
  let result = 0;
  for (i in s) {
    result += Number(s[i]);
  }
  return result;
}
