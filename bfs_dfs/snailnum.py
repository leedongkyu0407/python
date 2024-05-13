#테스트케이스 개수
T = int(input())

#범위 확인 함수 
def in_range(x, y, n):
    return x >= 0 and x < n and y>=0 and y < n

#정답출력 함수
def print_ans(map_list, n, tc):
    print('#', end='')
    print(tc)
    for i in range(n):
        for j in range(n):
            print(map_list[i][j], end = ' ')
        print() 
    return
 
#우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
 
for test_case in range(1, T+1):
    n = int(input())
    maps = [[0]*n for _ in range(n)]
 
    x, y = 0, 0
    direct_num = 0
    maps[x][y] = 1
    cnt = 2
 
    while True:
        if cnt > n*n:
            break
         
        nx, ny = x+dx[direct_num], y+dy[direct_num]
        if in_range(nx, ny, n) and maps[nx][ny] == 0:
                maps[nx][ny] = cnt
                cnt += 1            
                x, y = nx, ny
                  
        else:
            direct_num = (direct_num+1)%4
             
    print_ans(maps, n, test_case)