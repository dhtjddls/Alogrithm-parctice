function solution(lottos, win_nums) {
  let cnt = 0;
  let zeroCnt = 0;
  let floor = [46, 6, 5, 4, 3, 2];
  let result = [];
  for (let i = 0; i < lottos.length; i++) {
    if (win_nums.includes(lottos[i])) cnt += 1;
    if (lottos[i] === 0) zeroCnt += 1;
  }
  floor.indexOf(cnt + zeroCnt) === -1
    ? result.push(6)
    : result.push(floor.indexOf(cnt + zeroCnt));

  floor.indexOf(cnt) === -1 ? result.push(6) : result.push(floor.indexOf(cnt));

  return result;
}
