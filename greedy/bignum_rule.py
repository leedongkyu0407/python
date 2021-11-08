def input_check(n, nums): #입력값에 오류 있을시 false return
    if len(nums) != n:
        return False
    
    return True

def solution(n, m, k, nums):
    
    nums.sort() #정렬
    max = nums[-1] #가장 큰 수 
    second_max = nums[-2] # 두번째로 큰 수

    result = 0

    while True:
        for i in range(k):
            if m == 0: #m이 0이면 반복문 탈출
                break
            result += max
            m -= 1
        
        if m == 0:
            break
        result += second_max
        m -= 1
    return result

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

if input_check(n, nums):
    print(solution(n, m, k, nums))
else:
    print("잘못된 입력입니다.")