class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0 #number of boats 
        L, R = 0, len(people) - 1

        while L <= R:
            remain = limit - people[R]
            R -=1
            res +=1
            if L <= R and remain >= people[L]:
                L += 1
        return res