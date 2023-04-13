function solution(n, m) {
  function lcm(n, m) {
    if (n > m) [n, m] = [m, n];
    result = 0;
    while (true) {
      [m, n] = [n, m % n];
      if (n === 0) {
        result = m;
        break;
      }
    }
    return result;
  }

  function gcd(n, m, lcm) {
    return (n * m) / lcm;
  }
  let answer = [lcm(n, m), gcd(n, m, lcm(n, m))];
  return answer;
}
