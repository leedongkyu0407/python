import sys
def solution(input_s):
    #문자열만 따로 담기 위한 리스트 선언
    ch = []
    #숫자들만 더하기 위한 변수 선언
    num = 0

    #결과값 문자열을 담을 변수 선언
    result = ''

    for s in input_s:
        #문자열 중 숫자일 경우
        if s in '0123456789':
            num += int(s)
        else:
            ch.append(s)

    #문자열 오름차순 정렬
    ch.sort()

    for i in ch:
        result += i

    #숫자들을 더한 값도 결과 문자열 마지막에 추가
    if num != 0:
        result += str(num)

    return result

input_s = sys.stdin.readline().strip()

print(solution(input_s))
