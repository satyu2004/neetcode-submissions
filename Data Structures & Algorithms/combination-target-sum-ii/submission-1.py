class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = sorted(candidates)
        result = []
        n = len(candidates)

        def backtrack(curr_path, curr_sum, idx):
            if curr_sum == target:
                result.append(curr_path.copy())
                return
            if curr_sum > target:
                return
            
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if curr_sum + candidates[i] > target:
                    break
                    
                curr_path.append(candidates[i])
                backtrack(curr_path, curr_sum + candidates[i], i+1)
                curr_path.pop()
        
        backtrack([], 0, 0)
        return result