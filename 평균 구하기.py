def solution(arr):
    total = 0
    cnt =0
    for i in arr:
        total +=i
        cnt +=1

    answer = total / cnt
    return answer

# 파이썬 기본 내장 함수들을 사용하면 더 간단하게 풀 수 있음..
def solution2(arr):
    if(len(arr)==0):
        return 0
    else:
        return sum(arr)/len(arr)