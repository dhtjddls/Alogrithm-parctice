function solution(n, words) {
    var answer = [];
    let wordsArr = [];
    
  for (let i = 0; i < words.length; i++) {
    if (i === 0) wordsArr.push(words[i]);
    else if (
      words[i - 1][words[i - 1].length - 1] === words[i][0] && !wordsArr.includes(words[i])
    ) {
      wordsArr.push(words[i]);
    } else {
      return [(i % n) + 1, parseInt(i / n) + 1];
    }
  }
  return [0, 0];

}

function followUpValidation(beforeWord, afterWord){
    if (beforeWord.at(-1) === afterWord.at(0)) return true;
    else return false;
}

function wordDuplicateValidation(wordsArr, word){
    return 
}