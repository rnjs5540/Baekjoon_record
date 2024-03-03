def solution(fees, records):
    
    def getTimeDiff(tIn, tOut):
        tInHour, tInMinute = tIn.split(':')
        tOutHour, tOutMinute = tOut.split(':')
        tInHour = int(tInHour)
        tInMinute = int(tInMinute)
        tOutHour = int(tOutHour)
        tOutMinute = int(tOutMinute)
        
        tInMinute += 60 * tInHour
        tOutMinute += 60 * tOutHour
        
        return tOutMinute - tInMinute
    
    
    answer = []
    totalTimes = {}
    inTimes = {}
    for record in records:
        time, number, inout = record.split()
        if inout == 'IN':
            inTimes[number] = time
        else:
            if number not in totalTimes:
                totalTimes[number] = 0
            totalTimes[number] += getTimeDiff(inTimes[number], time)
            inTimes[number] = -1
    
    # 출차 안한 차 체크
    for number, inTime in inTimes.items():
        if number not in totalTimes:
                totalTimes[number] = 0
        if inTime != -1:
            totalTimes[number] += getTimeDiff(inTime, '23:59')
    
    # sort
    totalTimes = dict(sorted(totalTimes.items()))
    
    # 돈계산
    defaultTime = int(fees[0])
    defaultFee = int(fees[1])
    unitTime = int(fees[2])
    unitFee = int(fees[3])
    
    for number, totalTime in totalTimes.items():
        totalTime = int(totalTime)
        money = 0
        totalTime -= defaultTime
        money += defaultFee
        
        while totalTime > 0:
            totalTime -= unitTime
            money += unitFee
        answer.append(money)
        
    
    return answer