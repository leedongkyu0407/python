#보드의 크기 사과 개수 입력 받기
board_size = int(input())
apple = int(input())

#보드 생성
board = [[0]*board_size for _ in range(board_size)]

#보드에 사과 위치 -1로 세팅
for a in range(apple):
    line, row = map(int, input().split())
    board[line-1][row-1] = -1

#방향전환 횟수 입력
direction_change = int(input())
#dictionary 자료형을 이용하여 시간을 키로 방향 저장
direction = {}
for i in range(direction_change):
    s,d = input().split()
    direction[int(s)] = d

#메인 함수    
def solution(board, direction):        
    #초기 세팅
    sec = 0
    board[0][0] = 1
    #현재 뱀이 차지하고 있는 좌표 리스트
    snake_matrix = [[0,0]]
    #현재 방향
    direct_now = 0
    #사과 유무 확인용 플래그
    apple_flag = 0
    #R, D, L, U
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    #현재 x, y좌표
    nx = 0
    ny = 0

    while True:
        sec += 1
        x = nx + dx[direct_now]
        y = ny + dy[direct_now]
        #뱀이 벽에 부딪히거나 자기 자신과 부딪힐 경우 종료
        if (x > len(board)-1) or x < 0 or (y > len(board)-1) or y < 0 or board[x][y] == 1:
            return sec
        
        #사과가 있을 경우 플래그 설정 
        if board[x][y] == -1:
            apple_flag = 1
        #머리 다음 칸으로 이동    
        board[x][y] = 1
        snake_matrix.append([x, y])

        #사과가 없으면 꼬리가 위치한 칸 비우기
        if apple_flag != 1:
            px, py = snake_matrix.pop(0)
            board[px][py] = 0
        else:
            apple_flag = 0

        #방향 전환해야하는 시간일 경우
        if sec in direction.keys():
            if direction[sec] == 'D':
                direct_now += 1
            else:
                direct_now -= 1
            #dx, dy 리스트 활용을 위해 4로 나눈 나머지 활용    
            direct_now %= 4
            
        nx = x
        ny = y
    return

print(solution(board, direction))