# 149. Max Points on a Line. Hard. 16.2%.

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """        
        def nok(a,b): # Наибольший общий делитель.
            a, b = max(a, b), min(a, b)
            while (a % b) != 0:
                a -= (a // b) * b
                a, b = b, a
            return b
        
        
        def line(p,q): # Переводит две точки в None, если это одна и та же, либо в закодированную информацию о прямой,
            if p == q:      # на которой они лежат: первым идет кортеж, в котором представлен тангенас наклона прямой,   
                return None     # во втором точка, через которую прямая проходит.
            if p[0] == q[0]:            # Если прямая параллельна оси, то эта точка - ее пересеченье с другой осью.     
                return ((0,1),(p[0],0)) # Если нет - ближайшая к оси X снизу целочислвенная точка.
            if p[1] == q[1]:
                return ((1,0),(0,q[0]))
            if p[0] > q[0]:
                p, q = q, p
            k = ((q[1] - p[1]) // nok(q[0] - p[0], abs(q[1] - p[1])), (q[0] - p[0]) // nok(q[0] - p[0],abs(q[1] - p[1])))
            b = list(p)
            if p[1] <= 0:
                d = abs(p[1]) // k[0]
                b[0] += d * k[1]
                b[1] += d * k[0]
            else:
                d = p[1] // k[0]
                if p[1] % k[0] == 0:
                    b[1] = 0
                    b[0] -= d * k[1]
                else:
                    b[0] -= (d + 1) * k[1]
                    b[1] -= (d + 1) * k[0]                
            return (k,tuple(b))

        char = {} # Словарь, хранящий кратные точки.
        for p in points:
            if tuple(p) in char:
                char[tuple(p)] += 1
            else:
                char[tuple(p)] = 1

        if len(char) < 2: # Разбор случаев, когда нет двух различных точек.
            if len(char):
                return char[tuple(points[0])]
            else:
                return 0
        
        lines = {}      # Составляем словарь, ключи которого - коды прямых для каждой пары разлличных точек. Значения по ключам - 0.
        for a in char:
            for b in char:
                l = line(a,b)
                if l != None and l not in lines:
                    lines[l] = 0

        def isOnLine(l,p):  # Программа, получающая на вход кол прямой и точку, и отвечающая, лежит ли точка на прямой.
            k = l[0]
            b = l[1]
            if k == (0,1):
                return p[0] == b[0]
            elif k == (1,0):
                return p[1] == b[1]
            else:
                return p == b or (p[0] - b[0]) * k[0] == (p[1] - b[1]) * k[1]

        for l in lines:     # Для каждой точки из словаря кратных точек и для каждой прямой применяем предыдущую программу и подсчитываем,
            for p in char:  # сколько точек на какой прямой лежит.
                if isOnLine(l,p):   
                    lines[l] += char[p]
        answer = 0          # Ищем наибольшее значение по ключам в словаре с кодами прямых.
        for l in lines:
            if lines[l] > answer:
                answer = lines[l]
        return answer
