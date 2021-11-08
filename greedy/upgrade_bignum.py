def input_check(n, nums): #입력값에 오류 있을시 false return
    if len(nums) != n:
        return False
    
    return True

#개선된 큰 수의 법칙(그리디 알고리즘)
def upgrade_sol(n, m, k, nums):
    nums.sort() #정렬
    max = nums[-1]
    second = nums[-2]

    #가장 큰 수가 더해지는 횟수
    count = (m // (k+1)) * k
    count += m % (k + 1)

    result = 0
    result += (count * max) #가장 큰 수들의 합 구하기
    result += (m - count) * second # 두 번째로 큰 수들의 합 구하기

    return result

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

if input_check(n, nums):
    print(upgrade_sol(n, m, k, nums))
else:
    print("잘못된 입력입니다.")
