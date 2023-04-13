function solution(s, n) {
  const alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ];

  const bigAlphabets = alphabets.map((e) => e.toUpperCase());
  const alphabetsLength = alphabets.length;
  s = s.split("");
  for (i in s) {
    if (alphabets.includes(s[i])) {
      s[i] = alphabets[(alphabets.indexOf(s[i]) + n) % alphabetsLength];
    } else if (bigAlphabets.includes(s[i])) {
      s[i] = bigAlphabets[(bigAlphabets.indexOf(s[i]) + n) % alphabetsLength];
    }
  }

  return s.join("");
}
