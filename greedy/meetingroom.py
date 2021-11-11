def solution(n, meeting):
    meeting.sort(key = lambda x: (x[1], x[0]))

    result = 1

    finish = meeting[0][1]

    for i in range(1, n):
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
