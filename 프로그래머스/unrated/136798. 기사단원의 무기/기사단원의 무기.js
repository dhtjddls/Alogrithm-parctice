function solution(number, limit, power) {
    var answer = 0;
    let divisorArr = [];
    
    function getDivisorCount(num){
            let cnt = 0;
            for(let i = 1 ; i <= Math.sqrt(num) ; i++){
                if(num % i === 0) {
                    cnt += 1
                    if(num / i != i) cnt += 1
                }
            }
        return cnt;
    }
    
    for (let i = 1; i < number+1; i++){
        if (limit < getDivisorCount(i)) divisorArr.push(power)
        else divisorArr.push(getDivisorCount(i))
    }
    
    answer = divisorArr.reduce((a, b) => a + b, 0)
    
    return answer;
}

