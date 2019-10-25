# s - строка, q - запросы [left,right,k] вида "можно ли поменять k символов из подстроки s[left,right], чтоб строка стала полиндромом?"
# задача получена неправильным прочтением другой задачи.

class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        first = -1
        last = -1
        problems = 0
        for i in range(len(s) // 2):
            if s[i] != s[-1 -i]:
                if problems == 0:
                    first = i
                problems += 1
                last = i
        answer = []
        for q in queries:
            answer.append(((q[0] <= first and q[1] >= last) or (q[0] >= len(s) - 1 - first and q[1] <= len(s) - 1 - last)) and q[2] >= problems)
        return answer   
