//

function solution(s) {
  var answer = "";
  if (s.length % 2) {
    //  odd
    answer = s[Math.floor(s.length / 2)];
  } else {
    // even
    let mid = Math.floor(s.length / 2) - 1;
    answer = s.slice(mid, mid + 2);
  }
  return answer;
}
