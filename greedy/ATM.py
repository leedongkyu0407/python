def solution(n, data):
    data.sort()

    result = 0

    for i in range(len(data)):
        result += (data[i] * (n  - i))

    return result

n = int(input())
data = list(map(int, input().split()))

print(solution(n, data))

