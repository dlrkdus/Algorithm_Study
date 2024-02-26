s=list(input())
arr=[]
sum=1
ans=0

for i in range(len(s)):
    if s[i]=="(":
        sum*=2
        arr.append(s[i])
    elif s[i]=="[":
        sum*=3
        arr.append(s[i])
    elif s[i]==")":
        if len(arr)==0 or arr[-1]!="(":
            ans=0
            break
        if s[i-1]=="(":
            ans+=sum
        sum//=2
        arr.pop()
    else:
        if len(arr)==0 or arr[-1]!="[":
            ans=0
            break
        if s[i-1]=="[":
            ans+=sum
        sum//=3
        arr.pop()


if arr:
    ans=0
print(ans)