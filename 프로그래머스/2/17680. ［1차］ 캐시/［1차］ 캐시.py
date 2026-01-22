def solution(cacheSize, cities):
    answer = 0
    
    def is_cache_hit(cache, city, turn):
        if city in cache.keys():
            cache[city] = turn
            return True
        else:
            if len(cache) < cacheSize: # 캐시 용량 안 찼으면 추가
                cache[city] = turn
            else:
                update_cache(cache, city, turn) # 캐시 용량 꽉 찼으면 캐시 업데이트
            return False
    
    def update_cache(cache, city, turn):
        items = sorted(cache.items(), key=lambda v: v[1], reverse=False)
        if items:
            o_k, o_v = items[0] # 가장 예전에 들어온 캐시 찾기
            del cache[o_k] # 삭제
            cache[city] = turn # 새로운 캐시로 교체
        
    cache = {}
    for i, city in enumerate(cities):
        city = city.lower()
        if is_cache_hit(cache, city, i):
            answer += 1
        else:
            answer += 5
    
    return answer