function solution(participant, completion) {
  participant = participant.sort();
  completion = completion.sort();

  for (let i = 0; i < completion.length; i++) {
    if (participant[i] !== completion[i]) {
      return participant[i];
    }
  }
  return participant[participant.length - 1];
}
// p : 12345
// c : 1234
// 참가자 배열, 완주자 배열 정렬 =>
//
