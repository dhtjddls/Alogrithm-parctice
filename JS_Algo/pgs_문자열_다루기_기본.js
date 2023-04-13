function solution(s) {
  let answer = false;
  if (s.length === 4 || s.length === 6) {
    for (let i = 0; i < s.length; i++) {
      if (!isNaN(s[i]) === false) return (answer = false);
      answer = true;
    }
    // number -> 지수로 표기로 읽을 수 있으면 '10e1'
  }
  return answer;
}
