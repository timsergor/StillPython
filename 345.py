# Yandex interveiw 2.0.2.

# Дано бинарное дерево, ключи в котором - символы A-Z. Найти пару узлов дерева, таких что множеста символов ключей из поддеревьев с корнем в этих вершинах совпадают, а сумма размеров этих поддеревьев - максимальна.

def findNodeCouple(root):

    q = {}
    
    def SetAndSize(node):
        if not node:
            return (set(),0)
        if node in q:
            return q[node]
        L = SetAndSize(node.left)
        R = SetAndSize(node.right)
        return (L[0].union(R[0]), L[1] + R[1])
        
    char = {}
    
    def solution(node):
        C = SetAndSize(node)
        k = list(C[0])
        k.sort()
        k = tuple(k)
        if k not in char:
            char[k] = [(C[1], node)]
        else:
            char[k].append((C[1], node))
        if node.left:
            solution(node.left)
        if node.right:
            solution(node.right)
    
    solution(root)
    
    def realmin(m):
        if  len(m) == 1:
            return m[0][0]
        else:
            return min(m[0][0], m[1][0])
            
    mx = 0
    answer = None
    for k in char:
        m = []
        for c in char[k]:
            if len(m) < 2:
                m.append(c)
            elif c[0] > realmin(m):
                if m[0][0] == realmin(m):
                    m.pop(0)
                else:
                    m.pop(1)
                m.append(c)
        if m[0][0] + m[1][0] > mx:
            mx = m[0][0] + m[1][0]
            answer = (m[0][1], m[1][1])
    return answer
