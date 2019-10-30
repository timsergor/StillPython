# 692. Top K Frequent Words. 47.6%.

# Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

class wordheap(list):
    
    def __init__(self, k):
        self.size = 0
        self.limit = k
        
    def up(self, i):
        while i > 0 and (self[(i - 1) // 2][1] == "*" or self[(i - 1) // 2][1] > self[i][1] or (self[(i - 1) // 2][1] == self[i][1] and self[(i - 1) // 2][0] < self[i][0])):
            self[(i - 1) // 2], self[i] = self[i], self[(i - 1) // 2]
            i = (i - 1) // 2
    
    def cut(self):
        this = list(self[0])
        self[0][1] = "*"
        t = 0
        while t * 2 + 1 < len(self):
            if t * 2 + 2 >= len(self) or self[t * 2 + 2][1] == "*" or self[t * 2 + 1][1] != "*" and (self[t * 2 + 1][1] < self[t * 2 + 2][1] or (self[t * 2 + 1][1] == self[t * 2 + 2][1] and self[t * 2 + 1][0] > self[t * 2 + 2][0])):
                self[t], self[t * 2 + 1] = self[t * 2 + 1], self[t]
                t = t * 2 + 1
            else:
                self[t], self[t * 2 + 2] = self[t * 2 + 2], self[t]
                t = t * 2 + 2
        while self and self[-1][1] == "*":
            self.pop()
        self.size -= 1
        return this
    
    def push(self, x):
        if self.size < self.limit or x[1] >= self[0][1]:
            if len(self) and self[-1][1] == "*":
                self[-1] = x
            else:
                self.append(x)
            self.up(len(self) - 1)
            self.size += 1
            if self.size > self.limit:
                self.cut()
            print(self)
    

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        char = {}
        for word in words:
            if word in char:
                char[word] += 1
            else:
                char[word] = 1
                
        heap = wordheap(k)
        for c in char:
            heap.push([c,char[c]])
        answer = []
        while heap:
            w = heap.cut()
            if w[1] != "*":
                answer.append(w[0])
        answer.reverse()
        return answer
