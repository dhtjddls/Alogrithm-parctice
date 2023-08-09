function solution(name, yearning, photo) {
    const nameYearningObj = {}
    const result = []
    for (let i = 0; i < name.length; i++){
        nameYearningObj[name[i]] = yearning[i]
    }
    
    console.log(nameYearningObj)
    
    for (let i = 0; i < photo.length; i++){
        let totalYearning = 0
        photo[i].forEach((name) => {
            if (nameYearningObj[name]) totalYearning += nameYearningObj[name]  
        })
        result.push(totalYearning)
    }
    
    return result;
}