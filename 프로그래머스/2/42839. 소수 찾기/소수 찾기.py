import math
from itertools import permutations

def solution(numbers):
    answer = 0
    num = []
    result = set()
    for n in numbers:
        result.add(int(n))
        num.append(int(n))
        
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            result.add(num)
            
    
    def isPrime(n):
        if n<2:
            return False
        for i in range(2,int(math.sqrt(n)) + 1):
            if n%i==0:
                return False
        return True
    
    print(result)
    
    for r in result:
        if isPrime(r):
            answer+=1
    return answer