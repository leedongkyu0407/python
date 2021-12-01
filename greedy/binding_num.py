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

def solution(ls_PN, ls_NN, result):
    if (len(ls_PN) % 2) == 0:
        for j in range(0, len(ls_PN), 2):
            result += (ls_PN[j] * ls_PN[j+1])
    else:
        for j in range(0, len(ls_PN)-1, 2):
            result += (ls_PN[j] * ls_PN[j+1])
        result += ls_PN[-1]

    if (len(ls_NN) % 2) == 0:
        for k in range(0, len(ls_NN), 2):
            result += (ls_NN[k] * ls_NN[k+1])
    else:
        for k in range(0, len(ls_NN)-1, 2):
            result += (ls_NN[k] * ls_NN[k+1])
        result += ls_NN[-1]

    return result

n = int(sys.stdin.readline())

ls_PN, ls_NN, result = setting(n)
print(solution(ls_PN, ls_NN, result))
