#격자 범위 확인 함수
def in_range(x, y, n):
    return x>=0 and x<n and y >=0 and y<n

def solution(board, h, w):
    #상우하좌
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    target = board[h][w]
    answer = 0
    for i in range(4):
        #상하좌우 점이 격자 내에 위치하고
        if in_range(h+dxs[i], w+dys[i], len(board)):
            #색이 같다면
            color = board[h+dxs[i]][w+dys[i]]
            if target == color:
                answer += 1
    
    return answer