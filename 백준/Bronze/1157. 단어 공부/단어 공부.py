word = input().upper()
word_list = list(set(word))

arr = []
for w in word_list:
    c = word.count(w)
    arr.append(c)

m = max(arr)

if arr.count(m)>=2:
    print("?")
else:
    print(word_list[(arr.index(m))])





