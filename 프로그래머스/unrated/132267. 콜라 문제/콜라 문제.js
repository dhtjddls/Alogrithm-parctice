function solution(a, b, n) {
    let filledCoke = 0;
    let emptyCoke = n;
    let canExchangeCnt = a;
    
    while (emptyCoke >= canExchangeCnt) {
        let tempFilledCoke = Math.floor(emptyCoke / canExchangeCnt) * b
        filledCoke += tempFilledCoke
        emptyCoke = emptyCoke % canExchangeCnt + tempFilledCoke
        
    }   
    return filledCoke
}