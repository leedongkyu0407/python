def solution(n):
    result = 0

    while n >= 0:
        if n % 5 == 0:
            result += (n//5)
            return result        

        n -= 3
        result += 1

    return -1

n = int(input())

print(solution(n))
