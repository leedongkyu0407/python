import sys
def solution(num_ls):
    num_ls.sort(reverse = True)

    result = 0
    answer = ''

    #30의 배수이려면 10으로 나누어져야 하므로 맨 마지막 자리는 0이어야만 한다.
    if num_ls[-1] != 0:
        return -1    
    
    #10으로 나눈 나머지들이 3의 배수이려면 각 자릿수의 합이 3의 배수여야 한다.
    for i in num_ls:
        result += i
    
    if result%3 != 0:
        return -1
    
    #가장 큰 수를 구하는 것이므로 큰 수부터 앞자리를 채운다.
    for i in num_ls:
        answer += str(i)

    return answer 

n = sys.stdin.readline().strip()

num_ls = []

for i in n:
    temp = int(i)
    num_ls.append(temp)

print(solution(num_ls))