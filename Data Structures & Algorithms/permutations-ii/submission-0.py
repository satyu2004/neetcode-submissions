class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        def backtrack(current_path, used):
            if len(current_path) == len(nums):
                result.add(tuple(current_path))
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # if i^th number unused, use it 
                used[i] = True
                current_path.append(nums[i])

                # move along recursively
                backtrack(current_path, used)

                # undo last steps
                used[i] = False
                current_path.pop()


        used = [False] * len(nums)
        backtrack([], used)
        return list(result)