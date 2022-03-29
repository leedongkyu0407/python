def solution(n, build_frame):
    answer = []
    
    for bf in build_frame:
        x, y, kind, is_install = bf[0], bf[1], bf[2], bf[3]
        #설치
        if is_install == 1:
            if check_install(bf, answer) == True:
                answer.append([x, y, kind])
                
        #삭제
        elif is_install == 0:
            answer.remove([x,y,kind])
            #먼저 삭제한 뒤 check_delete 함수를 통해 남은 기둥과 보가 규칙을 만족하는지 확인
            if check_delete(bf, answer) == False:
                #규칙을 만족하지 못할 경우 삭제한 기둥 혹은 보를 재설치
                answer.append([x, y, kind])
    
    return sorted(answer)

#구조물 설치 함수
def check_install(bf, answer):
    x, y, kind = bf[0], bf[1], bf[2]
    #설치하는 게 기둥일 경우
    if kind == 0:        
        #바닥 위 or 보의 한 쪽 끝부분 위 or 다른 기둥 위이면 설치 가능
        if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
            return True
        else:
            return False

    #설치하는 게 보일 경우
    elif kind == 1:
        #보의 한 쪽 끝부분이 다른 기둥 위 or 양 쪽 끝부분이 다른 보와 동시에 연결되어있을 경우 설치 가능 
        if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
            return True        
        else:
            return False

#구조물 삭제 뒤 남은 구조물이 규칙을 만족하는지 확인하는 함수
def check_delete(bf, answer):
    for x, y, kind in answer:
        #설치된 게 기둥일 경우
        if kind == 0:        
            #바닥 위 or 보의 한 쪽 끝부분 위 or 다른 기둥 위이면 유지 가능
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False

        #설치된 게 보일 경우
        elif kind == 1:
            #보의 한 쪽 끝부분이 다른 기둥 위 or 양 쪽 끝부분이 다른 보와 동시에 연결되어있을 경우 유지 가능 
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue            
            return False
    
    return True
