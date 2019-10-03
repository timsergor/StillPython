if len(nums) == 0:
            return -1
        
        def search(l,r):
            if r - l < 2:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1
            if nums[l] < nums[r]:
                if r - l < 2:
                    if nums[l] == target:
                        return l
                    else:
                        return r
                else:
                    if nums[(l + r) // 2] > target:
                        return search(l, ((l + r) // 2) - 1)
                    elif nums[(l + r) // 2] < target:
                        return search(((l + r) // 2) + 1, r)
                    else:
                        return (l + r) // 2
            else:
                if nums[(l + r) // 2] > nums[l]: 
                    if target >= nums[l] and target <= nums[(l + r) // 2]:
                        return search(l,(l + r) // 2)
                    else:
                        return search(((l + r) // 2) + 1, r)
                else:
                    if target >= nums[(l + r) // 2] and target <= nums[r]:
                        return search(((l + r) // 2), r)
                    else:
                        return search(l,(l + r) // 2)
        
        return search(0,len(nums) - 1)
        
# 25min.
