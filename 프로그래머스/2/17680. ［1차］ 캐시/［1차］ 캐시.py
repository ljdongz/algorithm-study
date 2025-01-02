
def solution(cacheSize, cities):
    answer = 0

    caches = []

    for city in cities:
        ct = city.upper()
        if ct in caches:
            answer += 1
            caches.remove(ct)
            caches.append(ct)
        else:
            if len(caches) < cacheSize:
                caches.append(ct)
                answer += 5
            elif cacheSize == 0:
                answer += 5
            else:
                caches = caches[1:]
                caches.append(ct)
                answer += 5

    return answer