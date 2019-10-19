# 1228. Missing Number In Arithmetic Progression. Easy. Contest.

# In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

# Then, a value from arr was removed that was not the first or last value in the array.

# Return the removed value.

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if arr[1] > arr[0]:
            if arr[2] - arr[1] < arr[1] - arr[0]:
                return arr[0] + arr[2] - arr[1]
            d = arr[1] - arr[0]
            for i in range(1,len(arr) - 1):
                if arr[i + 1] - arr[i] > d:
                    return arr[i] + d
        elif arr[1] < arr[0]:
            if arr[2] - arr[1] > arr[1] - arr[0]:
                return arr[0] + arr[2] - arr[1]
            d = arr[1] - arr[0]
            for i in range(1,len(arr) - 1):
                if arr[i + 1] - arr[i] < d:
                    return arr[i] + d
        else:
            return arr[0]
            
# ~ 6 min.
