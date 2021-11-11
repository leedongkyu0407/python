import sys

def solution(n, A, B):
    A.sort()

    result = 0
    '''S가 가장 작아지려면 A중 가장 작은 것과
    B 중 가장 큰 것을 곱해주면 된다.
    '''
    for i in A:
        result += (i * max(B))
        B.remove(max(B))

    return result

n = int(sys.stdin.readline())

A = list(map(int, (sys.stdin.readline().split())))
B = list(map(int, (sys.stdin.readline().split())))

print(solution(n, A, B))
