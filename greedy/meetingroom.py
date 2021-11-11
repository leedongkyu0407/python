import sys

def solution(n, meeting):
    '''notion에 상세 설명
    이중 리스트에서 두 번째 원소 기준 오름차순 정렬 후 
    첫번째 원소 기준 오름차순 정렬
    '''
    meeting.sort(key = lambda x: (x[1], x[0]))
    
    finish = meeting[0][1]
    #배정된 회의 개수
    result = 1

    for i in range(1, n):
        #앞선 회의가 끝나는 시간 이후에 시작하는 회의
        if finish <= meeting[i][0]:
            result += 1
            finish = meeting[i][1]

    return result

n = int(sys.stdin.readline())

meeting = [[0]*2 for _ in range(n)]

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meeting[i][0] = start
    meeting[i][1] = end

print(solution(n, meeting))
