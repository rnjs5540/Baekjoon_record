def solution(s):
    answer = 0
    munja = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    while len(s) > 0:
        if s[0].isdigit():
            answer *= 10
            answer += int(s[0])
            s = s[1:]
        else:
            for i, el in enumerate(munja):
                if s.find(el) == 0:
                    answer *= 10
                    answer += i
                    s = s[len(el):]
                    break
                
    return answer