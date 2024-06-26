n=int(input())

words = [str(input()) for i in range(n)]

words = list(set(words))    #중복값 제거
words.sort()                #사전순 정렬(str이니까)
words.sort(key=len)         #길이순대로 다시 정렬

for i in words:
    print(i)
