class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = list(s)
        palindrome = [i.lower() for i in palindrome if i.isalnum()]
        return palindrome == palindrome[::-1]