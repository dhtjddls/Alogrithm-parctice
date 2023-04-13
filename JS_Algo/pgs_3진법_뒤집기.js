function solution(n) {
  n = n.toString(3);
  n = parseInt(n.split("").reverse("").join(""), 3);
  return n;
}
