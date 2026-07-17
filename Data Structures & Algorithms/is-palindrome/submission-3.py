class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""

        for word in s:
            if word.isalnum():
                forward += word.lower()
        return forward == forward[::-1]