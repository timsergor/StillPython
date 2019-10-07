# 372. Super Pow. Medium. 35.9%.

# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        map = [a % 1337]
        A = ((a % 1337) ** 10) % 1337
        for i in range(min(1336,len(b) - 1)):
            map.append(A)
            A = ((A % 1337) ** 10) % 1337
        b.reverse()
        print(map)
        answer = 1
        for i in range(len(b)):
            answer = (answer * map[i % 1337] ** b[i]) % 1337
        return answer
