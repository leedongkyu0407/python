import sys
def solution(num_ls):
    num_ls.sort(reverse = True)

    result = 0
    answer = ''

    #30의 배수이려면 10으로 나누어져야 하므로 맨 마지막 자리는 0이어야만 한다.
    if num_ls[-1] != 0:
        return -1    
    
    for i in num_ls:
        result += i
    
    if result%3 != 0:
        return -1
    
    for i in num_ls:
        answer += str(i)

    return answer 

n = sys.stdin.readline().strip()

num_ls = []

for i in n:
    temp = int(i)
    num_ls.append(temp)

print(solution(num_ls))