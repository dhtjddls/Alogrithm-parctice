function solution(nums) {
  let answer;
  let kind = [...new Set(nums)];
  kind.length <= nums.length / 2
    ? (answer = kind.length)
    : (answer = Math.round(nums.length / 2));
  return answer;
}
