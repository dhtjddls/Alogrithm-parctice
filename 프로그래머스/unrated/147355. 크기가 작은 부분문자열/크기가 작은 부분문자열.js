function solution(t, p) {
    let subStringLength = p.length;
    let answer = 0;
    
    for (let i = 0; i < t.length - subStringLength + 1; i++){
        let tSubString = Number(t.slice(i,i+subStringLength))
        let pSubString = Number(p)
        
        if (tSubString <= pSubString) {
            answer += 1
            }
    }
    
    
    
    return answer;
}