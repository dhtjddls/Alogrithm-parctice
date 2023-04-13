function solution(n) {
  var answer = 0;
  function sosu(num) {
    if (num === 1 || num === 0) return false;
    if (num === 2 || num === 3) return true;
    if (num % 2 === 0 || num % 3 === 0) return false;
    for (let i = 2; i < Math.floor(Math.sqrt(num)) + 1; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }
  for (let i = 1; i <= n; i++) {
    if (sosu(i)) answer += 1;
  }

  return answer;
}
