class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False
    
    def addword(self,word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.EndOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addword(w)
        
        row = len(board)
        col = len(board[0])
        res = set()
        visited = set()


        def dfs(r,c,node,word):
            if (r < 0 or r >= row or c <0 or c >= col or (r,c) in visited or board[r][c] not in node.children):
                return 
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.EndOfWord:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)



            visited.remove((r,c))

        for r in range(row):
            for c in range(col):
                dfs(r,c,root,'')
        return list(res)
        