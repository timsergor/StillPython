# 412. Fizz Buzz. 60.1%.

# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(1,n + 1):
            if i % 3 and i % 5:
                answer.append(str(i))
            elif i % 5:
                answer.append("Fizz")
            elif i % 3:
                answer.append("Buzz")
            else:
                answer.append("FizzBuzz")
        return answer
        
# 3min.
