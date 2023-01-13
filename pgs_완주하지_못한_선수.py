def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = list()
    for i in range(len(participant)):
        if i == len(participant)-1:
            answer.append(participant[i])
        elif participant[i] != completion[i]:
            answer.append(participant[i])
            break
    
    
        
    
    return answer[0]