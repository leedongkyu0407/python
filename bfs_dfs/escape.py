from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#상, 하, 좌, 우 이동좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    #큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        #현재 노드에서 상, 하, 좌, 우 위치의 노드 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #미로를 벗어날 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            #괴물이 있을 시 무시(지나갈 수 없음)
            if graph[nx][ny] == 0:
                continue
            
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    #출구의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0, 0))
