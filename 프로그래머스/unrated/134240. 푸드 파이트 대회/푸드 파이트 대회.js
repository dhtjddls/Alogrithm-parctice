function solution(food) {
//     food들을 짝수로 만든 후, 갯수로 변환
    let answer = '';
    for (let i = 1; i < food.length; i++){
        if (food[i] % 2 !== 0){
            food[i] -= 1
        }
        food[i] /= 2
        
        if (food[i] !== 0) answer += String(i).repeat(food[i])
    }

    answer = answer + '0' + answer.split('').reverse().join('')
    
    
    
    return answer;
    
}