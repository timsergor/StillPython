# 1209. Remove All Adjacent Duplicates in String II. Medium. Contest.

# Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        symbols = []
        lengths = []
        i = 0
        while i < len(s):
            if symbols == []:
                symbols.append(s[i])
                lengths.append(1)
                i += 1
            else:
                if s[i] != symbols[-1]:
                    if lengths[-1] >= k:
                        t = k
                        x = symbols[-1]
                        while symbols and symbols[-1] == x and t:
                            symbols.pop()
                            t -= 1
                        if symbols and symbols[-1] == x:
                            lengths[-1] -= k
                        else:
                            lengths.pop()
                    else:
                        symbols.append(s[i])
                        lengths.append(1)
                        i += 1
                else:
                    symbols.append(s[i])
                    lengths[-1] += 1
                    i += 1
        if lengths and lengths[-1] >= k:
            t = k
            x = symbols[-1]
            while symbols and symbols[-1] == x and t:
                symbols.pop()
                t -= 1
            if symbols and symbols[-1] == x:
                lengths[-1] -= k
            else:
                lengths.pop()
        return "".join(symbols)

# 25min.
