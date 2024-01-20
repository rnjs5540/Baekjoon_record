def getDist(loc1, loc2):
    print(loc1, loc2, abs(loc1[0] - loc2[0]) + abs(loc1[1]))
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
    # print(loc1, loc2, pow(loc1[0]-loc2[0],2) + pow(loc1[1]-loc2[1], 2))
    # return pow(loc1[0]-loc2[0],2) + pow(loc1[1]-loc2[1], 2)

def solution(numbers, hand):
    answer = ''
    lloc = [3,0]
    rloc = [3,2]
    for number in numbers:
        if number == 0:
            number = 11
        nloc = [(number-1)//3, (number-1)%3]
        if nloc[1] == 0:
            answer += 'L'
            lloc = nloc
            continue
        elif nloc[1] == 2:
            answer += 'R'
            rloc = nloc
            continue
        
        ldist = getDist(nloc, lloc)
        rdist = getDist(nloc, rloc)
        print(number)
        if ldist < rdist or (ldist == rdist and hand == 'left'):
            print('l')
            answer += 'L'
            lloc = nloc
        else:
            print('r')
            answer += 'R'
            rloc = nloc
        
    return answer