def solution(s):
    to_0 = 0 #전부 0으로 뒤집는 경우
    to_1 = 0 #전부 1로 뒤집는 경우

    #첫번째 원소 처리
    if s[0] == '0':
        to_1 += 1
    else:
        to_0 += 1

    #두 번째 원소부터 모든 원소를 차례로 확인
    for i in range(1, len(s)):
        
        if s[i-1] != s[i]:

            #다음 수에서 1로 바뀌는 경우
            if s[i] == '1':
                to_0 += 1

            #다음 수에서 0으로 바뀌는 경우
            else:
                to_1 += 1
                
    # 둘 중 더 적은 수 반환
    return min(to_0, to_1)

s = input()

print(solution(s))