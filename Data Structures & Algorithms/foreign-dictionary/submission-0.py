class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = collections.defaultdict(set)
        nodes = set()
        for w in words:
            nodes |= set(w)
        for i in range(len(words)-1):
            word1,word2 = words[i],words[i+1]
            minlen = min(len(word1),len(word2))
            if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
                return ""
            for j in range(minlen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        
        visit = set()
        cycle = set()
        res = []

        def dfs(char):
            if char in cycle:
                return False
            
            if char in visit:
                return True
            
            cycle.add(char)
            for nei in adj[char]:
                if not dfs(nei):
                    return False
            
            cycle.remove(char)
            visit.add(char)
            res.append(char)
            return True



        for c in nodes:
            if not dfs(c):
                return ""
        
        res = res[::-1]

        return "".join(res)