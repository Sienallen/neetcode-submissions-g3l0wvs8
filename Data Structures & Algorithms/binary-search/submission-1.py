class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binary (low, high):
            
            if (high >= low):
                mid = low + (high - low)//2
                if(nums[mid] == target):
                    return mid

                elif( nums[mid] > target):
                    return binary(low, mid - 1 )
                
                elif(nums[mid] < target):
                    return binary(mid + 1, high)

            return -1

            
        return binary(0, len(nums)-1)