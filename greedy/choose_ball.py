def solution(data):
    case = 0 # 가능한 경우의 수

    #앞에서부터 하나를 선택했을 시 가능한 경우의 수 추가
    for i in range(len(data)-1):
        for j in range(i+1, len(data)): 
            if data[i] != data[j]:
                case += 1

    return case

def solution_upgrade(n, m, data):
    #1부터 10까지의 무게를 담을 수 있는 리스트
    check = [0] * 11

    #무게별 볼링공 개수 세기
    for i in data:
        check[i] += 1

    case = 0
    #1부터 m까지 각 무게에 대해 처리
    for j in range(1, m+1):
        #무게가 j인(A가 선택한 공의 무게와 동일한) 볼링공의 개수 제외
        n -= check[j]
        #B가 선택할 수 있는 경우의 수 곱하기
        case += check[j] * n 

    return case

n, m = map(int, input().split())

data = list(map(int, input().split()))

print(solution(data))
print(solution_upgrade(n, m, data))