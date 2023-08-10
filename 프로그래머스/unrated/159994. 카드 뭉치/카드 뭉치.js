function solution(cards1, cards2, goal) {
    let cardOneIdx = [];
    let cardTwoIdx = [];
    
    for (let i = 0; i < goal.length; i++) {
        if (cards1.includes(goal[i])){
            cardOneIdx.push(cards1.indexOf(goal[i]))
        }
        if (cards2.includes(goal[i])){
            cardTwoIdx.push(cards2.indexOf(goal[i]))
        }
    }
    
    for (let i = 1; i < cardOneIdx.length; i++){
        if (cardOneIdx[i] - 1 !== cardOneIdx[i-1]) return 'No'
    }
    
    for (let i = 1; i < cardTwoIdx.length; i++){
        if (cardTwoIdx[i] - 1 !== cardTwoIdx[i-1]) return 'No'
    }
    
    return 'Yes'
}