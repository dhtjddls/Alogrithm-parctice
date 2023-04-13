function solution(price, money, count) {
  var answer = 0;
  let totalPrice = 0;
  for (let i = 1; i <= count; i++) {
    totalPrice += i * price;
  }
  if (money < totalPrice) answer = totalPrice - money;
  return answer;
}
