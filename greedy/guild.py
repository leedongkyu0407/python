def solution(data):
    result = 0 #여행을 떠나는 그룹 수
    data.sort()

    count = 0 #현재 그룹에 속하는 모험가의 수

    for i in data: #공포도가 낮은 것부터 순차적으로 확인
        count += 1 #현재 그룹에 해당 모험가 추가
        if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면 그룹 결성 
            result += 1 #그룹 수 증가
            count = 0 # 현재 그룹에 포함된 모험가 수 초기화

    return result

n = int(input())
data = list(map(int, input().split()))

print(solution(data))
