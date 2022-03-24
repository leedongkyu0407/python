def solution(key, lock):
    n = len(key)
    m = len(lock)
    #확장 정사각형 한 변의 길이
    padding_len = m + 2*(n-1)

    padding_lock = [[0]*padding_len for _ in range(padding_len)]

    #확장 정사각형 중앙에 자물쇠 배치
    for i in range(m):
        for j in range(m):
            padding_lock[n-1+i][n-1+j] = lock[i][j] 

    limit = padding_len - n + 1
    #열쇠 돌리며 체크
    for rotate in range(4):
        key = rotate_90(key)
        #열쇠 시작 포인트 
        for x in range(limit):
            for y in range(limit):
                #열쇠 끼우기
                for i in range(n):
                    for j in range(n):
                        padding_lock[x+i][y+j] += key[i][j]
                #자물쇠에 열쇠가 맞는지 확인
                if check(padding_lock, n, x, y) == True:
                    return True
                #열쇠 빼기
                for i in range(n):
                    for j in range(n):
                        padding_lock[x+i][y+j] -= key[i][j]
    return False

#배열 90도 회전 함수
def rotate_90(a):
    n = len(a)
    res = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            res[j][n-i-1] = a[i][j]
    
    return res

#열쇠로 자물쇠가 열리는지 확인
def check(padding_lock, n, x, y):
    for i in range(n):
        for j in range(n):
            if padding_lock[x+i][y+j] != 1:
                return False
    
    return True