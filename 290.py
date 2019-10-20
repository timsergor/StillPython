# 1233. Remove Sub-Folders from the Filesystem. Medium. Contest.

# Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

# If a folder[i] is located within another folder[j], it is called a sub-folder of it.

# The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = len)
        char = {}
        
        def pref(a,b):
            if len(a) < len(b):
                for i in range(len(a)):
                    if a[i] != b[i]:
                        return False
                if b[len(a)] == "/":
                    return True
            return False
        
        for i in range(len(folder)):
            Flag = True
            for j in range(len(folder[i])):
                if j > 0 and folder[i][j] == "/" and folder[i][0:j] in char:
                    Flag = False
                    break
            if Flag:
                char[folder[i]] = True
        
        return list(char)
