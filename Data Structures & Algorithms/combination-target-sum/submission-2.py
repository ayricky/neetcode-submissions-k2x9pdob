class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result, subset = [], []

        def dfs(i, curr_sum):
            if curr_sum == target:
                result.append(subset.copy())
                return

            for j in range(i, len(nums)):
                if curr_sum + nums[j] > target:
                    return

                subset.append(nums[j])
                dfs(j, curr_sum + nums[j])
                subset.pop()


        dfs(0, 0)
        return result