class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        str1=s[::-1].split()
        str1.sort()
        result=[]
        for i in str1:
            result.append(i[1:][::-1])
        return " ".join(result)