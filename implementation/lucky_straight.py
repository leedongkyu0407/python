import sys
def solution(score):
    #점수를 반으로 나누어 왼쪽과 오른쪽 분리하기
    left = score[:len(score)//2]
    right = score[len(score)//2:]

    result = 0

    #왼 쪽의 각 자릿수의 합을 result에 더하기
    for i in left:
        result += int(i)

    #result에 더해진 왼쪽의 각 자릿수의 합에서 오른쪽 각 자릿수의 합을 빼기
    for j in right:
        result -= int(j)

    #두 수의 합이 같다면 LUCKY 반환
    if result == 0:
        return "LUCKY"

    else:
        return "READY"

score = sys.stdin.readline().strip()
print(solution(score))