class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums = set(nums)
        result = []
        N = len(nums)

        def dfs(subset, last_index):
            if last_index == N:
                result.append(subset)
                return

            dfs(subset, last_index+1)
            dfs(subset + [nums[last_index]], last_index+1)



        dfs([], 0)
        return result
        