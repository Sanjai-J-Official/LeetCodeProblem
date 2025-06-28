class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack :
            return haystack.find(needle)               
        else :
            return -1
#return haystack.find(needle) if needle in haystack else -1
