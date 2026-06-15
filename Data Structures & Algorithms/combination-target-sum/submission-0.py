class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(current_path, idx, current_sum):
            if current_sum >= target:
                if current_sum == target:
                    result.append(current_path.copy())
                return
            
            for i in range(idx, len(nums)):
                current_path += [nums[i]]
                # attach idx to path
                backtrack(current_path, i, current_sum + nums[i])
                # step back
                current_path.pop()

            

                
        backtrack([], 0, 0)
        return result