n, m = map(int, input().split())

result = 0

for i in range(n): #한 줄씩 입력받아 min 찾기
    data = list(map(int, input().split()))
    min_num = min(data)

    #가장 작은 수들 중 가장 큰 수 찾기
    result = max(result, min_num)

print(result)
