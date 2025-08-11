class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def binSearch(arr, currL):
            l, r = 0, len(arr) - 1
            while l < r:
                mid = l + (r - l)//2
                if arr[mid] <= currL:
                    l = mid + 1
                else:
                    r = mid
            if arr[r] > currL:
                return arr[r]
            return -1
                
        indices = collections.defaultdict(list)
        n = len(source)
        for i in range(n):
            indices[source[i]].append(i)

        r = 0
        currL = -1 #current pointer in target
        res = 0
        for r in range(len(target)):
            if target[r] not in indices:
                return -1
            nextIdx = binSearch(indices[target[r]], currL)
            if nextIdx == -1: #could not find the next s[r] in source, need to restart
                res += 1
                currL = indices[target[r]][0]
            else:
                currL = nextIdx
        return res + 1