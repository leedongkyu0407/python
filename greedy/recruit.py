import sys
def setting():
    #t로 주어진 입력값만큼 반복하기 위해 입력을 함수로 분리
    n = int(sys.stdin.readline())

    rank_ls = [[0]*2 for i in range(n)]

    for i in range(n):
        first, second = map(int, sys.stdin.readline().split())
        rank_ls[i][0] = first
        rank_ls[i][1] = second
    #문제 입력으로 들어오는 n과 시험 등수 리스트를 반환
    return n, rank_ls

def solution(n, rank_ls):
    #1차 시험 기준으로 정렬
    rank_ls.sort(key = lambda x: x[0])
    #1차 시험 기준으로 정렬 시 가장 앞의 참가자(1등)는 무조건 합격
    pass_num = 1
    comparison = rank_ls[0][1]

    for i in range(1, n):
        sec_rank = rank_ls[i][1]
        #1차 시험은 이길 수 없으므로 2차 시험 기준으로 비교하여
        #등수가 더 낮을 시 불합격
        if sec_rank > comparison:
            continue
        else:
            pass_num += 1
            comparison = sec_rank

    return pass_num

t = int(sys.stdin.readline())

#케이스만큼 반복
for i in range(t):
    n, rank_ls = setting()
    print(solution(n, rank_ls))