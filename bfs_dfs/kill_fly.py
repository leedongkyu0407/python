T = int(input())

#범위확인 함수
def in_range(x, y, n):
        return x>=0 and x<n and y>=0 and y<n

for tc in range(1, T+1):
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
 
    max_fly = 0
    #0,0 기준점부터 전체 탐색
    for i in range(n):
        for j in range(n):
            fly = 0
            #mXm 크기의 파리채
            for x in range(i, i+m):
                for y in range(j, j+m):
                    if in_range(x, y, n):
                        fly += maps[x][y]
             
            max_fly = max(max_fly, fly)
    print('#%d %d' %(tc, max_fly))