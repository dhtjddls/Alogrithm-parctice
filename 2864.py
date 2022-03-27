a, b = input().split()
min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min, max)

# replace라는 함수를 전혀 떠올리지를 못했따..ㅠㅠㅠ 문자열을 돌면서 5가나오면 6으로 바꿔주는 혹은 6이나오면 5로 바꿔주는 그리고 인트로 변환하는 방법이 있었겠다
