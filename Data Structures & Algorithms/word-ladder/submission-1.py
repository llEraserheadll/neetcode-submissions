class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        map = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                map[pattern].append(word)
        
        q = collections.deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        dist = 1
        while q:
            qlen = len(q)
            for i in range(qlen):
                word = q.popleft()
                if word == endWord:
                    return dist
                for j in range(len(word)):
                    pattern = word[:j]+'*'+word[j+1:]
                    for nei in map[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)

            dist += 1
        return 0
            

