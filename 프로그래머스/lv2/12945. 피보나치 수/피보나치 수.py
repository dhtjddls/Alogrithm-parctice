def solution(n):
    answer_list = [0] * 100002
    answer_list[0], answer_list[1] = 0, 1
    for i in range(2, 100001):
        answer_list[i] = answer_list[i-1] + answer_list[i-2]
    return answer_list[n] % 1234567