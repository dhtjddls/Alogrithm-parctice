// pP pCount yY yCount
function solution(s) {
  s = s.toLowerCase();
  let pCnt = s.length - s.replaceAll("p", "").length;
  let yCnt = s.length - s.replaceAll("y", "").length;
  if (pCnt === yCnt) return true;
  else return false;
}
