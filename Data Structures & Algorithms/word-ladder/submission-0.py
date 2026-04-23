class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)

        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                nei[pattern].append(word)
        
        visit = set()
        q = collections.deque()
        q.append((beginWord))
        visit.add((beginWord))

        dist = 1
        while q:
            qlen = len(q)
            for i in range(qlen):
                word = q.popleft()
                if word == endWord:
                    return dist
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            dist += 1
        return 0


