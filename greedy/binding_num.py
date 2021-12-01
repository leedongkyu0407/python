import sys
def setting(n): #초기 세팅
    ls_PN = []
    ls_NN = []

    result = 0

    for i in range(n):
        temp = int(sys.stdin.readline())
        if temp > 1:
            ls_PN.append(temp)
        elif temp == 1:
            result += 1
        else:
            ls_NN.append(temp)

    ls_PN.sort(reverse=True)
    ls_NN.sort()

    return ls_PN, ls_NN, result


def solution(ls_N, result):
    if (len(ls_N) % 2) == 0:
        for j in range(0, len(ls_N), 2):
            result += (ls_N[j] * ls_N[j+1])
    else:
        for j in range(0, len(ls_N)-1, 2):
            result += (ls_N[j] * ls_N[j+1])
        result += ls_N[-1]#원소 개수가 홀수일 경우 마지막 원소 더하기

    return result

n = int(sys.stdin.readline())

ls_PN, ls_NN, result = setting(n)
result = solution(ls_PN, result)
print(solution(ls_NN, result))