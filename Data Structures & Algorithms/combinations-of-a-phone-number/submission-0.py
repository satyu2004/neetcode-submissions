class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        result = []
        if len(digits) == 0: return result

        dictionary = {'2':['a', 'b', 'c'],
        '3':['d', 'e', 'f'],
        '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'],
        '6':['m', 'n', 'o'],
        '7':['p', 'q', 'r', 's'],
        '8':['t', 'u', 'v'],
        '9':['w', 'x', 'y', 'z']
        }


        def backtrack(curr_path, idx):
            if idx == len(digits):
                result.append("".join(curr_path))
                return

            for char in dictionary[digits[idx]]:
                curr_path.append(char)
                backtrack(curr_path, idx+1)
                curr_path.pop()
            

        backtrack([], 0)

        return result