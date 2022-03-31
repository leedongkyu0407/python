from itertools import permutations

def solution(n, weak, dist):
    #최소값 비교를 위해 9 할당
    answer = 9

    #반시계 방향 회전을 고려하기 위해 길이를 두 배로 늘려 일자 리스트로 구성
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    
    #친구 투입 경우의 수(순열)
    dist_perm = list(permutations(dist, len(dist)))

    #시작 포인트
    for start in range(length):
        #경우의 수마다 계산
        for dp in dist_perm:
            #투입하는 친구 수
            cnt = 1
            #투입한 사람의 마지막 위치
            end = weak[start] + dp[cnt-1]
            #모든 취약점이 도는지 확인
            for i in range(start, start+length):
                #마지막 위치가 취약점 위치보다 낮을 경우 친구 한 명 추가 투입
                if end < weak[i]:
                    cnt += 1
                    #투입할 수 있는 친구가 없다면 다음 경우의 수로 이동
                    if cnt > len(dist):
                        break
                    #다음 투입한 사람의 마지막 위치 계산
                    end = weak[i] + dp[cnt-1]
            #기존의 답보다 더 적은 인원을 투입했다면 answer값 변경
            answer = min(answer, cnt)
    
    #반복문 종료 후 answer가 투입 가능한 사람보다 클 경우 답 없음(-1) 리턴
    if answer > len(dist):
        return -1

    return answer
