function solution(x) {
  let s = String(x);
  let sum = 0;
  for (i in s) {
    sum += Number(s[i]);
  }
  if (x % sum == 0) {
    return true;
  } else {
    return false;
  }
}

// string 바꾸고 -> 자릿수합 구하고 % 함 == 0 일때 true 아닐때 false
