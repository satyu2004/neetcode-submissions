class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        N = len(nums)

        def dfs(subset, last_index):
            if last_index == N:
                result.add(tuple(subset))
                return
            
            dfs(subset, last_index+1)
            dfs(subset + [nums[last_index]], last_index+1)


        dfs([], 0)
        return list(result)
        