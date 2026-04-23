class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = collections.defaultdict(list)
        for src,dst in sorted(tickets)[::-1]:
            edges[src].append(dst)

        res = []

        def dfs(src):
            while edges[src]:
                dst = edges[src].pop()
                dfs(dst)

            res.append(src)


        dfs('JFK')
        return res[::-1]
