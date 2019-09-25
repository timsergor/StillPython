# 165. Compare Version Numbers. Medium. 24.8%.

# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

# You may assume that the version strings are non-empty and contain only digits and the . character.

# The . character does not represent a decimal point and is used to separate number sequences.

# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        V1 = version1.split(".")
        V2 = version2.split(".")
        for i in range(len(V1)):
            if V1[i][0] != 0:
                V1[i] = int(V1[i])
            else:
                j = 0
                while j < len(V1[i]) and V1[i][j] == "0":
                    j += 1
                if j == len(V1[i]):
                    V1[i] = 0
                else:
                    V1[i] = int(V1[i][j:len(V1[i])])
        for i in range(len(V2)):
            if V2[i][0] != 0:
                V2[i] = int(V2[i])
            else:
                j = 0
                while j < len(V2[i]) and V2[i][j] == "0":
                    j += 1
                if j == len(V2[i]):
                    V2[i] = 0
                else:
                    V2[i] = int(V2[i][j:len(V2[i])])
        for i in range(min(len(V1),len(V2))):
            if V1[i] > V2[i]:
                return 1
            if V1[i] < V2[i]:
                return -1
        if len(V1) > len(V2):
            for i in range(len(V2),len(V1)):
                if V1[i] > 0:
                    return 1
            return 0
        if len(V2) > len(V1):
            for i in range(len(V1),len(V2)):
                if V2[i] > 0:
                    return -1
            return 0
        return 0
        
# 12min.
