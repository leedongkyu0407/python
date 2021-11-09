def solution(data):
    case = 0 # 가능한 경우의 수

    #앞에서부터 하나를 선택했을 시 가능한 경우의 수 추가
    for i in range(len(data)-1):
        for j in range(i+1, len(data)): 
            if data[i] != data[j]:
                case += 1

    return case

n, m = map(int, input().split())

data = list(map(int, input().split()))

print(solution(data))
