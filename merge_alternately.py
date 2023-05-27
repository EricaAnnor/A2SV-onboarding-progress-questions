class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        word = []
        i = 0
        
        while i < len(word1) and i < len(word2):
            word.append(word1[i])
            word.append(word2[i])
            i+=1


        if i < len(word1):
            word.extend(word1[i:])
        elif i < len(word2):
            word.extend(word2[i:])
        return "".join(word)
        
