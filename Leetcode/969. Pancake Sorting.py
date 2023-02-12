class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        a = []
        for unsorted in range(len(arr), 0, -1):
            i = arr.index(unsorted)
            if i == arr.index(unsorted) -1:
                continue
            
            arr = arr[unsorted - 1: i: -1] + arr[:i + 1] + arr[unsorted:]
            a += [i + 1, unsorted]
            
        return a