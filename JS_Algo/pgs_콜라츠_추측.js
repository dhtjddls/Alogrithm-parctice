function solution(num) {
  cnt = 0;
  if (num === 1) {
    return 0;
  }
  while (cnt !== 499) {
    num % 2 == 0 ? (num /= 2) : (num = num * 3 + 1);
    cnt += 1;
    if (num == 1) break;
  }
  if (cnt == 499) cnt = -1;
  return cnt;
}
