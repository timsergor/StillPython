#1010. Pairs of Songs With Total Durations Divisible by 60. Easy. 45.8%

#In a list of songs, the i-th song has a duration of time[i] seconds. 
#Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        char = {i:0 for i in range(60)}
        for i in range(len(time)):
            if (time[i] % 60) in char:
                char[time[i] % 60] += 1
        answer = 0
        for i in range(1,30):
            answer += char[i] * char[60 -i]
        answer += char[30] * (char[30] - 1) / 2
        answer += char[0] * (char[0] - 1) / 2
        return(int(answer))
        
# 10 min.
