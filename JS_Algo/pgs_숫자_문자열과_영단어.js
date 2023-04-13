function solution(s) {
  const strNums = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  const Nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
  for (i in strNums) {
    s = s.split(strNums[i]).join(Nums[i]);
  }
  return Number(s);
}
