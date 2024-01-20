def solution(cacheSize, cities):
    from collections import deque

    hit, miss = 0, 0
    cache = deque([])
    # cities.append(None)
    for city in cities:
        print(cache, "\t", city, city in cache)
        city = city.lower()
        if city in cache:
            cache.remove(city)
            # cache.appendleft(city)
            hit += 1
            print("HIT")
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop()
            miss += 1
            print("MISSED")
        cache.appendleft(city)

    answer = hit + miss * 5
    print(answer, hit, miss)
    return answer


solution(
    3,
    [
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
    ],
)

solution(
    3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
)

solution(
    2,
    [
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
        "SanFrancisco",
        "Seoul",
        "Rome",
        "Paris",
        "Jeju",
        "NewYork",
        "Rome",
    ],
)


from collections import OrderedDict


class Cache:
    def __init__(self, cachesize):
        self.size = cachesize
        self.cache = OrderedDict()

    def process_time(self, item):
        if self.cache.get(item):
            del self.cache[item]
            self.cache[item] = True
            return 1
        else:
            self.cache[item] = True
            if len(self.cache) > self.size:
                firstkey = list(self.cache.keys())[0]
                del self.cache[firstkey]
            return 5


def solution(cacheSize, cities):
    cache = Cache(cacheSize)
    return sum([cache.process_time(city.lower()) for city in cities])
