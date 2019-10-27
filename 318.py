# 1239. Maximum Length of a Concatenated String with Unique Characters. Medium. Contest.

# Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

# Return the maximum possible length of s.

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        scheme = []
        for i in range(len(arr)):
            scheme.append([dict()])
            for j in range(len(arr[i])):
                if arr[i][j] not in scheme[-1][0]:
                    scheme[-1][0][arr[i][j]] = True
                else:
                    scheme.pop()
                    break
        answer = 0
        for i in range(1,len(scheme)):
            start = dict(scheme[i][0])
            for j in range(i):
                for p in range(len(scheme[j])):
                    char = dict(scheme[j][p])
                    Flag = True
                    for c in char:
                        for d in start:
                            if c == d:
                                Flag = False
                                break
                        if not Flag:
                            break
                    if Flag:
                        if len(char) + len(start) >= len(scheme[i]):
                            for d in start:
                                char[d] = True
                            scheme[i].append(char)
        for i in range(len(scheme)):
            for j in range(len(scheme[i])):
                if len(scheme[i][j]) > answer:
                    answer = len(scheme[i][j])
        return answer
