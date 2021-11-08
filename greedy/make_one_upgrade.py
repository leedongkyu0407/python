import time

def solution(n, k):
    result = 0

    while True:
        #(n이 k로 나누어떨어지는 수가 될 때까지 1씩 빼기)
        target = (n // k) * k 
        result += (n - target)
        n = target

        #n이 k보다 작을 때 (더 이상 나눌 수 없을 때 반복문 탈출)
        if n < k:
            break

        #k로 나누기
        result += 1
        n //= k

    #마지막으로 남은 수에 대해 1씩 빼기
    result += (n - 1)
    return result

start_time = time.time()    
n, k = map(int, input().split())
print(solution(n, k))
end_time = time.time()
print("time : ", end_time - start_time)