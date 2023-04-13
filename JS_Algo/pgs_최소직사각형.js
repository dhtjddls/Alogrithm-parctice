function solution(sizes) {
  let max_w = 0;
  let max_h = 0;
  sizes.forEach((e) => {
    e.sort((a, b) => a - b);
    if (e[0] > max_w) max_w = e[0];
    if (e[1] > max_h) max_h = e[1];
  });
  return max_w * max_h;
}
