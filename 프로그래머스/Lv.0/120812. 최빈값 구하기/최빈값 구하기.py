def solution(array):
    answer = 0
    maxFre = 0
    dic = {}
    for el in array:
        if el in dic:
            dic[el] += 1
        else:
            dic[el] = 1
    
    for key, val in dic.items():
        if val > maxFre:
            maxFre = val
            answer = key
        elif val == maxFre:
            answer = -1
    
    if answer == -1:
        return answer
    return answer