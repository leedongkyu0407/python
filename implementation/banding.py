def recover(now_hp, bandage, health, continual):
    if continual == bandage[0]:
        recover = bandage[1]+bandage[2]
    else:
        recover = bandage[1]
        
    if now_hp + recover >= health:
        now_hp = health
    else:
        now_hp += recover

    return now_hp

def solution(bandage, health, attacks):
    answer = 0
    attack_t = attacks[-1][0]
    now_hp = health
    continual = 1
    attacks.reverse()
    
    for t in range(1, attack_t+1):
       #공격 매커니즘
        if t == attacks[-1][0]:
            now_hp -= attacks[-1][1]
            attacks.pop()
            continual = 1
            print(now_hp, t)
            if now_hp <= 0:
                return -1            
            continue

        print(continual)
        #회복 매커니즘
        now_hp = recover(now_hp, bandage, health, continual)    
        continual += 1

        if continual > bandage[0]:
            continual = 1
        print(now_hp ,t)
    return now_hp

bandage = [1, 1, 1]
health = 5
attacks = [[1, 2], [3, 2]]
print(solution(bandage, health, attacks))