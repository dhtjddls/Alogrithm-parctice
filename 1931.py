n = int(input())
meeting = []
for _ in range(n):
    k, v = map(int, input().split())
    meeting.append([k,v])

meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

max_meeting = 0
start = 0
for meet in meeting:
    if meet[0] >= start:
        start = meet[1]
        max_meeting += 1

print(max_meeting)