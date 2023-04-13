function solution(answers) {
  const playerOne = [1, 2, 3, 4, 5];
  const playerTwo = [2, 1, 2, 3, 2, 4, 2, 5];
  const playerThree = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  const oneLen = playerOne.length;
  const twoLen = playerTwo.length;
  const threeLen = playerThree.length;
  let score = [0, 0, 0];
  let result = [];

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === playerOne[i % oneLen]) score[0] += 1;
    if (answers[i] === playerTwo[i % twoLen]) score[1] += 1;
    if (answers[i] === playerThree[i % threeLen]) score[2] += 1;
  }
  for (i in score) {
    if (Math.max(...score) === score[i]) result.push(parseInt(i) + 1);
  }
  return result;
}
