// Date.getDay() 0-6
function solution(a, b) {
  var answer = "";
  let days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  // new Date('2016-a-b')
  let day = new Date(`2016-${a}-${b}`).getDay();
  answer = days[day];
  return answer;
}
