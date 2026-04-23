class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {
            '2':'abc',
            '3' :'def',
            '4' : 'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return []

        res = []

        def backtrack(index,path):
            if len(path) == len(digits):
                res.append(''.join(path))
                return 
            
            characters = char_map[digits[index]]

            for char in characters:
                path.append(char)
                backtrack(index+1,path)
                path.pop()



        backtrack(0,[])
        return res