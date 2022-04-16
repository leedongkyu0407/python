from collections import deque

n, m, k, x = map(int, input().split())
#해당 노드에서 출발해서 한 번의 이동만으로 도달 가능한 노드 번호
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(n+1)
#시작 노드는 방문처리
distance[x] = 0

#bfs 사용을 위한 queue 선언, 시작 노드를 먼저 queue에 추가
queue = deque()
queue.append(x)

while queue:
    #현재 노드
    now = queue.popleft()
    #현재 노드에 연결되어 있는 노드
    for next_node in graph[now]:
        #아직 방문한 적이 없을 경우
        if distance[next_node] == -1:
            queue.append(next_node)
            #노드 방문 처리 및 시작 노드부터 해당 노드까지의 거리 계산
            distance[next_node] = distance[now] + 1

check = False
for i in range(n+1):
    #출발 노드 x로부터 거리가 k인 모든 노드 번호 출력
    if distance[i] == k:
        print(i)
        check = True

#거리가 k인 노드가 없다면 -1 출력
if check == False:
    print(-1)
