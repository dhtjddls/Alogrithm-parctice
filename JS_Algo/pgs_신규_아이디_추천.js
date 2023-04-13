function solution(new_id) {
  new_id = new_id
    .toLowerCase()
    .replace(/[^a-z0-9-_.]/gi, "")
    // a-z까지,0-9까지,_.빼고고,/g(global) -> 문자열 전체, /i(insensitive) ->       대소문자 구별하지 않고,  ''로 바꾼다
    .replace(/\.{2,}/g, ".")
    // \ -> 매칭한다, .{2,} -> . 2개이상으로 이루어진 문자열을 /g -> 문자열 전체에     서, '.'로 바꾼다.
    .replace(/^\.|\.$/, "");
  //  ^\. -> 뒤에오는 .으로 시작하는 문자열을 매칭한다, | -> 혹은  \.$ -> .으로 끝나는 문자열을 매칭한다. ''로 바꾼다.
  if (new_id.length === 0) new_id = "a";
  // new_id가 빈 문자열이면 "a" 대입
  if (new_id.length >= 16) new_id = new_id.substring(0, 15);
  new_id = new_id.replace(/\.$/, "");
  //  \.$ -> .으로 끝나는 문자열을 매칭한다, ''로 바꾼다.
  if (new_id.length <= 2)
    new_id = new_id + new_id[new_id.length - 1].repeat(3 - new_id.length);
  return new_id;
}
