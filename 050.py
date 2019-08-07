#551. Student Attendance Record I. Easy. 45.5%.

#You are given a string representing an attendance record for a student. The record only contains the following three characters:
#'A' : Absent.
#'L' : Late.
#'P' : Present.
#A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
#You need to return whether the student could be rewarded according to his attendance record.

class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for i in range(len(s)):
            if s[i] == "A":
                a += 1
                l = 0
            elif s[i] == "L":
                l += 1
            else:
                l = 0
            if l > 2 or a > 1:
                return(False)
        return(True)
        
 # 5 min.
