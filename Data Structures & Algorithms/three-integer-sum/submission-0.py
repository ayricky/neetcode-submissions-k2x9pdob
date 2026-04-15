class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            # Sorted array allows us skip anything past 0 since adding anything > 0 will never == 0
            if num > 0: 
                break
            
            # Skip duplicate numbers
            if i > 0 and num == nums[i - 1]: 
                continue 

            L, R = i + 1, len(nums) - 1
            while L < R:
                three_sum = num + nums[L] + nums[R]
                if three_sum > 0:
                    R -= 1
                elif three_sum < 0:
                    L += 1
                else:
                    result.append([num, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while nums[L] == nums[L - 1] and L < R:
                        L += 1


        return result