import time
def solution(n, k):
    count = 0

    while n != 1:
        if n % k == 0: #n이 k로 나누어떨어지면 나누기
            n /= k
        else:   #n이 k로 나누어떨어지지 않으면 1씩 빼기
            n -= 1
        
        count += 1 #매 연산시 숫자 세기

    return count

start_time = time.time()

n, k = map(int, input().split())
print(solution(n, k))

end_time = time.time()
print("time : ", end_time - start_time)