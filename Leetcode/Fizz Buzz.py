class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(1, n+1):
            temp = ""
            if i % 3 ==0:
                temp += 'Fizz'
            if i % 5 == 0:
                temp += 'Buzz'
            if i % 3 !=0 and i % 5 !=0:
                temp += str(i)
            output.append(temp)
        return output