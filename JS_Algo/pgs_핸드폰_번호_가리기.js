//
function solution(phone_number) {
  var answer = "";
  start = phone_number.length - 4;
  answer += "*".repeat(start);
  answer += phone_number.substr(start, 4);

  return answer;
}
