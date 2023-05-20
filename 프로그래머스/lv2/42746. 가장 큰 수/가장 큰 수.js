function solution(numbers) {
    let strNums = numbers.map(a => a.toString())
    let answer = strNums.sort((a, b) => (b+a) - (a+b)).join("")
    
    return (answer[0] === "0") ? '0' : answer
}
