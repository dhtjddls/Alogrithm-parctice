
n = int(input())
answer = 0
enterQue = set()

for _ in range(n):
  cmd = input()
  if cmd == 'ENTER':
    answer += len(enterQue)
    enterQue = set()
  else:
    enterQue.add(cmd)
answer += len(enterQue)
print(answer)