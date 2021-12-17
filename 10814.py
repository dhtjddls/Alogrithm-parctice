user_list = []
N = int(input())
for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    user_list.append((age, name))

user_list.sort(key = lambda x : x[0])

for i in user_list:
    print(i[0], i[1])

# 특정한 부분만을 정렬하고 싶거나 사용하고 싶을때, lambda 식을 사용할 수 있음을 꼭꼭 기억하자. 그리고 처음에는 인덱싱을 해서 그냥 앞에 두글자만 받으려 했으나 나이가 한자리거나 세자리일 경우도 있기 때문에 나이는 나이로, 이름은 이름으로 나눠서 관리하는 것이 좋았다. 이것도 꼭 기억하자. 괜히 인덱싱으로 한정할 생각하지말고 정확한 역할별로 나누어서 생각하자.