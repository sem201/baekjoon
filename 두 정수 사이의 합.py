def solution(a, b):
    if(a>b):
        a,b = b,a
    if(a==b):
        return a
    else:
        sum = 0
        for i in range(a,b+1):
            sum +=i
        return sum
    
# 다른 방법
def adder(a,b):
    if(a>b):
      a,b = b,a
    return sum(range(a,b+1))