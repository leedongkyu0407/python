n = int(input())
k = int(input())

apple_matrix = [[0]*n for _ in range(n)]
snake_matrix = [[0]*n for _ in range(n)]

for i in range(k):
    row, col = map(int, input().split())
    apple_matrix[row-1][col-1] = 1

print(apple_matrix)

change_dir = int(input())
sec_dir = {}

for i in range(change_dir):
    s, d = input().split()
    sec_dir[int(s)] = d

snake_loc = [[0,0]]


def solution(apple_matrix, snake_matrix, sec_dir):
    sec = 1
    direction = 0

    while True:

        sec += 1

        if sec in sec_dir.keys():
            dir = sec_dir[sec]
            direction = check_dir(direction, dir)

        if direction < 0:
            return sec

        elif direction % 4 == 0:
            check = dir_0(apple_matrix, snake_matrix, snake_loc)

        elif direction % 4 == 1:
            check = dir_1(apple_matrix, snake_matrix, snake_loc)

        elif direction % 4 == 2:
            check = dir_2(apple_matrix, snake_matrix, snake_loc)

        elif direction % 4 == 3:
            check = dir_3(apple_matrix, snake_matrix, snake_loc)

        if check == False:
            return sec+1
        print(len(snake_matrix))
    return sec

def check_dir(direction, d):
    if d == 'D':
        direction += 1
    else:
        direction -= 1
    
    return direction

def dir_0(apple_matrix, snake_matrix, snake_loc):
    r, c = snake_loc[-1]
    if c+1 > len(snake_matrix)-1:
        return False
    
    elif snake_matrix[r][c+1] == 1:
        return False
    
    elif apple_matrix[r][c+1] != 1:
        prev_r, prev_c = snake_loc.pop(0)
        snake_matrix[prev_r][prev_c] = 0
    
    snake_matrix[r][c+1] = 1
    snake_loc.append([r, c+1])
    return 

def dir_1(apple_matrix, snake_matrix, snake_loc):
    r, c = snake_loc[-1]
    if r+1 > len(snake_matrix)-1:
        return False
    
    elif snake_matrix[r+1][c] == 1:
        return False
    
    elif apple_matrix[r+1][c] != 1:
        prev_r, prev_c = snake_loc.pop(0)
        snake_matrix[prev_r][prev_c] = 0
    
    snake_matrix[r+1][c] = 1
    snake_loc.append([r+1, c])
    return 

def dir_2(apple_matrix, snake_matrix, snake_loc):
    r, c = snake_loc[-1]
    if c-1 < 0:
        return False
    
    elif snake_matrix[r][c-1] == 1:
        return False
    
    elif apple_matrix[r][c-1] != 1:
        prev_r, prev_c = snake_loc.pop(0)
        snake_matrix[prev_r][prev_c] = 0
    
    snake_matrix[r][c-1] = 1
    snake_loc.append([r, c-1])
    return 

def dir_3(apple_matrix, snake_matrix, snake_loc):
    r, c = snake_loc[-1]
    if r-1 < 0:
        return False
    
    elif snake_matrix[r-1][c] == 1:
        return False
    
    elif apple_matrix[r-1][c] != 1:
        prev_r, prev_c = snake_loc.pop(0)
        snake_matrix[prev_r][prev_c] = 0
    
    snake_matrix[r-1][c] = 1
    snake_loc.append([r-1, c])
    return 

print(solution(apple_matrix, snake_matrix, sec_dir))

#어딘가에서 인덱스 관련 버그 생긴 듯 (디버깅 ㄱㄱ)