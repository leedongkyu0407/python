def solution(data):

    data.sort() #오름 차순으로 화폐 단위 정렬

    target = 1 #만들어야 하는 수

    for i in data:
        #만들 수 없는 금액을 찾을시 종료
        if target < i:
            break

        target += i

    return target

n = int(input())
data = list(map(int, input().split()))

print(solution(data))
