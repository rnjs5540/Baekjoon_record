def solution(N, stages):
    answer = []
    silpaeyuls = []
    reached = []
    nonCleared = []
    for i in range(N+2):
        reached.append(0)
        nonCleared.append(0)
    
    for stage in stages:
        for i in range(1, stage+1):
            reached[i] += 1
        nonCleared[stage] += 1
    
    for i in range(1, N+1):
        print(nonCleared[i], reached[i])
        if reached[i] == 0:
            silpaeyuls.append(0)
        else:
            silpaeyuls.append(nonCleared[i] / reached[i])
    print(silpaeyuls)
    
    myset = set(silpaeyuls)    
    sorted_myset = sorted(myset, reverse=True)
    print(sorted_myset)
    
    for val in sorted_myset:
        for i, silpaeyul in enumerate(silpaeyuls):
            if val == silpaeyul:
                answer.append(i+1)
    print(answer)
    
    # set에 값들 넣기
    # 중복제거된 값들 for문으로 다 찾아서 answer에 넣기
        
    return answer