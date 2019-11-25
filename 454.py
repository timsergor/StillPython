# 423. Reconstruct Original Digits from English. Medium. 46.2%.

# Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        char = {}
        for i in range(len(s)):
            if s[i] in char:
                char[s[i]] += 1
            else:
                char[s[i]] = 1
        for i in range(ord("a"), ord("z") + 1):
            if chr(i) not in char:
                char[chr(i)] = 0
        Key = [0] * 10
        Key[0] = char["z"]
        Key[2] = char["w"]
        Key[4] = char["u"]
        Key[6] = char["x"]
        Key[8] = char["g"]
        Key[1] = char["o"] - Key[0] - Key[2] - Key[4]
        Key[3] = char["t"] - Key[2] - Key[8]
        Key[5] = char["f"] - Key[4]
        Key[7] = char["s"] - Key[6]
        Key[9] = char["i"] - Key[5] - Key[6] - Key[8]
        pre = []
        for i in range(len(Key)):
            for j in range(Key[i]):
                pre.append(str(i))
        return "".join(pre)
