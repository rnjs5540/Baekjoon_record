def solution(cacheSize, cities):
    answer = 0
    # 캐시 맨 뒤가 LRU
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        # hit
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        # miss
        else:
            answer += 5
            if cacheSize > 0 and len(cache) >= cacheSize:
                del cache[0]
            cache.append(city)
    
    return answer