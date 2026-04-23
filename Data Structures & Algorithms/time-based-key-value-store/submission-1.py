class TimeMap:

    def __init__(self):

        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        l = 0
        r = len(values) - 1

        while l < r:
            mid = (l + r) // 2

            if values[mid][1] >= timestamp:
                r = mid
            else:
                l = mid + 1
        
        if values[l][1] > timestamp:
            return values[l-1][0] if l - 1 >= 0 else ""


        return values[l][0]
        
