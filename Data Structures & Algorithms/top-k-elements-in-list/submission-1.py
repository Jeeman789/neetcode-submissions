class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elems = {}
        for i in nums:
            if i not in elems:
                elems[i] = 1
            else:
                elems[i] += 1
        sorted_dict = heapq.nlargest(k, elems, key=elems.get)
        return sorted_dict