def solution(s):
    result = int(s[0]) #제일 앞의 숫자

    for i in range(1, len(s)):
        num = int(s[i])

        if num <= 1 or result <= 1: #더하거나 곱해야 하는 두 수중 어느 하나라도 0이거나 1이면 더하기 실행
            result += num
        else:
            result *= num

    return result

s = input()

print(solution(s))