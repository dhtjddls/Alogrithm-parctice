import itertools
def solution(numbers):
    answer = []
    numbers_list = list(numbers)
    per_list = []
    for i in range(1, len(numbers_list) + 1):
        per_list += (list(itertools.permutations(numbers_list, i)))
    new_nums = [int(("").join(p)) for p in per_list]  
    for n in new_nums:                           
        if n < 2:                                
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):      
            if n % i == 0:                        
                check = False
                break
        if check:
            answer.append(n)                     
    return len(set(answer))