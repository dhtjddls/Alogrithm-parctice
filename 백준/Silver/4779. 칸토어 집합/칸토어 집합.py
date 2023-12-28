def cantor(n):
  if n == 1:
    return '-'
  else:
    left = cantor(n // 3)
    center = ' ' * (n // 3)
    return left + center + left

while True:
  try:
    n = int(input())
    
    result = cantor(3**n)
    print(result)
  except:
    break