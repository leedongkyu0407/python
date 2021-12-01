import sys
def solution(n, list_rp):
    #추후 계산의 편의를 위해 역순 정렬
    list_rp.sort(reverse=True) 
    answer_ls = []

    #notion에 설명
    for i in range(n):
        temp = list_rp[i]*(i+1)
        answer_ls.append(temp)

    return max(answer_ls)

n = int(sys.stdin.readline())
list_rp = []

for i in range(n):
    temp = int(sys.stdin.readline())
    list_rp.append(temp)

print(solution(n, list_rp))
