class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(current_path, used):
            if len(current_path) == len(nums):
                result.append(current_path.copy())
                return
            
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                
                used[i] = True
                current_path.append(nums[i])

                backtrack(current_path, used)

                current_path.pop()
                used[i] = False



        used = [False] * len(nums)
        backtrack([], used)
        return result