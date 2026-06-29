class TimeMap:

    def __init__(self):
        self.storage = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        test = self.storage.get(key, [])

        print(test)
        l , r = 0 , len(test) - 1

        while l <= r:
            m = (l+r) // 2
            if test[m][1] <= timestamp:
                ans = test[m][0]
                l = m + 1
            else:
                r =  m - 1

        return ans


