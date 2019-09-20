# 935. Knight Dialer. Medium. 41.9%.
# A chess knight can move as indicated in the chess diagram below:
# ***
# This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.
# Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.
# How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.nightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        map = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        lastdigit = [1,1,1,1,1,1,1,1,1,1]
        for counter in range(N - 1):
            step = [0,0,0,0,0,0,0,0,0,0]
            for i in range(10):
                for j in range(len(map[i])):
                    step[map[i][j]] += lastdigit[i]
            lastdigit = step
        return sum(lastdigit) % (10**9 + 7)
