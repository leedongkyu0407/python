def solution(n):
    result = 0

    while n >= 0:
        #n이 5로 나누어 떨어지면 나눈 뒤 몫을 횟수에 더해서 반환
        if n % 5 == 0:
            result += (n//5)
            return result        

        #n이 5로 나누어 떨어지지 않을 때는 횟수를 1씩 추가하며 3씩 뺴준다.
        n -= 3
        result += 1

    #while문 종료 후에도 반환이 되지 않았다면 해가 존재하지 않음
    return -1

n = int(input())

print(solution(n))
