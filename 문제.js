// 직사각형 별찍기

// 5 3
//
process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const input = data.split(" ");
  const n = Number(input[0]),
    m = Number(input[1]);
  for (let i = 0; i < m; i++) {
    let starString = "*".repeat(n);
    console.log(starString);
  }
});
