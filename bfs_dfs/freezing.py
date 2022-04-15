n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드 방문
def dfs(x, y):
    #범위 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    #아직 방문하지 않았다면(얼음틀의 비어있는 공간이라면)
    if graph[x][y] == 0:
        #해당 노드 방문 처리(음료수 채우기)
        graph[x][y] = 1
        #상, 하, 좌, 우의 노드를 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True
    
    return False

#모든 노드에 대해 음료수 채울 수 있는지 확인
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 수행(연결된 노드들의 개수 구하기)
        if dfs(i, j) == True:
            result += 1

print(result)