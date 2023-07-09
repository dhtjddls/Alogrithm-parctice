def solution(progresses, speeds):
    answer = []
    end_day = []
    for i in range(len(progresses)):
        rest = (100 - progresses[i]) % speeds[i]
        if rest == 0:
            end_day.append((100 - progresses[i]) // speeds[i])
        else:
            end_day.append((100 - progresses[i]) // speeds[i] + 1)

    deploy_list = []
    max_task = end_day[0]
    cnt = 0
    for i in range(1, len(end_day)):
        if max_task < end_day[i]:
            max_task = end_day[i]
            answer.append(cnt+1)
            cnt = 0
        else:
            cnt += 1
    answer.append(cnt+1)

    return answer