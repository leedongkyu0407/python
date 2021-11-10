def solution(n, k, data):
    #역순(내림차순)으로 정렬
    data.sort(reverse = True)
    result = 0 #코인 개수 

    for i in range(n):
        if k == 0:
            break
        #큰 것부터 확인하며 잔돈 계산
        if data[i] <= k:
            #몫은 코인 개수 
            result += (k // data[i])
            k %= data[i]

    return result

n, k = map(int, input().split())

#코인 종류 저장 리스트
data = [0] * n

for i in range(n): #코인 입력값 저장
    data[i] = int(input())

print(solution(n, k, data))