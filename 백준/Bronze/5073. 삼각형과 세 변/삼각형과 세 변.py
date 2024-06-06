
while(True):
    a, b, c = map(int,input().split())
    arr = [a,b,c]
    if a==0 and b==0 and c==0:
        break
    if max(arr)>= sum(arr)-max(arr):
        print("Invalid")
        continue
    if a!=b and b!=c and c!=a:
        print("Scalene")
        continue
    if a==b and b==c and c==a:
        print("Equilateral")
        continue
    if a==b and a!=c or b==c and b!=a or a==c and c!=b:
        print("Isosceles ")


