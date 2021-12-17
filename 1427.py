N = list(input())
map(int, N)
arr = []
for i in N:
    arr.append(int(i))
arr.sort(reverse=True)
for i in arr:
    print(i,end='')

# 직접 정렬을 계속 이용하다가 이미있는 정렬 기능을 이용하니 참 편했다. 전에 공부할때 적어놓은 자릿수 별 값을 얻고싶을 때 사용하는 방법인 map함수를 이용해서 문자열을 숫자열로 바꾸면 자리별로 나눠진다는 것을 이용하여 문제를 풀었다.
