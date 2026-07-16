class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(l, r):
            if (r >= l): 
                mid = l + (r - l) // 2
                if (nums[mid] == target):
                    return mid
                
                elif (nums[mid] > target):
                    return binary(l, mid-1)
                elif (nums[mid] < target):
                    return binary(mid + 1, r)
            else: 
                return -1
        
        right = len(nums)-1
        return binary(0, right)
