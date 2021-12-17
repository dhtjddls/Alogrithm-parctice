def word_reverser(t: int):
    for _ in range(t):
        word = list(input().split())

        for i in word:
            print(i[::-1], end=" ")
        print()
       

t = int(input())
word_reverser(t)