function solution(k, score) {
    const honorArr = []
    const result = []
    for(let i = 0 ; i < score.length ; i ++) {
        if(i < k) {
            honorArr.push(score[i])
        }
        if(score[i]>Math.min(...honorArr)) {
            honorArr.pop()
            honorArr.push(score[i])
            honorArr.sort((a,b) => b-a)
        }
        result.push(honorArr[honorArr.length-1])
    }
    return result
}