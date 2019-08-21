#973. K Closest Points to Origin. Medium. 61.5%.

#We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#(Here, the distance between two points on a plane is the Euclidean distance.)
#You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(P):
            return(P[0]**2 + P[1]**2)
        
        points.sort(key = dist)
        answer = [points[i] for i in range(K)]
        return(answer)
        
# also max heap
