import sys
def solution(data):
    #나이트 초기 위치
    row = int(data[1])
    column = int(ord(data[0])) - int(ord('a')) + 1

    #나이트가 이동할 수 있는 모든 방향
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    #각 방향에 대해 이동 가능한지 확인
    count = 0
    for step in steps:
        #이동하고자 하는 위치 확인
        next_row = row + step[0]
        next_column = column + step[1]

        #해당 위치로 이동 가능하면 카운트 증가
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            count += 1


    return count

data = sys.stdin.readline()

print(solution(data))
 