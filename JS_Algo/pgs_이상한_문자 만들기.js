// split -> forEach()
function solution(s) {
  let result = "";
  s = s.split(" ");

  s.forEach((e) => {
    if (e == "") {
      result += " ";
    } else {
      for (let i = 0; i < e.length; i++) {
        i % 2 === 0
          ? (result += e[i].toUpperCase())
          : (result += e[i].toLowerCase());
        if (i < e.length) result += " ";
      }
    }
  });
  // "try   hello".split(" ")
  // [try, " ", " ", "hello"]
  // e1 = e.replaceAll(" ", "")
}

// console.log(solution("try   hello"))
// TrY   HeLlO

function solution(s) {
  let result = "";
  s = s.split(" ");

  for (let i = 0; i < s.length; i++) {
    for (let j = 0; j < s[i].length; j++) {
      j % 2 === 0
        ? (result += s[i][j].toUpperCase())
        : (result += s[i][j].toLowerCase());
    }
    if (i < s.length - 1) result += " ";
  }
  return result;
}
