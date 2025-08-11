class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        freqMap = collections.Counter(tops)
        for i in bottoms:
            freqMap[i] += 1
        n = len(tops)
        targetNum = -1
        for num, count in freqMap.items():
            if count >= n:
                targetNum = num
        if targetNum == -1:
            return -1
            
        topR, bottmR = 0, 0
        for i in range(len(tops)):
            if tops[i] != targetNum and bottoms[i] != targetNum:
                return -1
            if tops[i] != targetNum:
                topR += 1
            if bottoms[i] != targetNum:
                bottmR += 1
        return min(topR, bottmR)