#406. Queue Reconstruction by Height. Medium. 60.7%.
#Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
#Note:
#The number of people is less than 1,100.

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def height(human):
            return(human[0])
        
        people.sort(key = height)
        answer = []
        char = {}
        for i in range(len(people)):
            for j in range(len(people)):
                if people[j][0] not in char:
                    char[people[j][0]] = 0
                    for c in char:
                        if c > people[j][0] and char[c] > char[people[j][0]]:
                            char[people[j][0]] = char[c]
                if char[people[j][0]] == people[j][1]:
                    answer.append(people[j])
                    for c in char:
                        if c <= people[j][0]:
                            char[c] += 1
                    people.pop(j)
                    break
        return answer
