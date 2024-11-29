def solution(n):
    n = list(map(str,str(n)))
    n.sort()
    n.reverse()
    return int(''.join(map(str,n)))

# 참고 코드 1.
def solution(n):
    ls = list(str(n))
    ls.sort(reverse=True)
    return int("".join(ls))

# 참고 코드 2. (정렬 알고리즘 이용)
  