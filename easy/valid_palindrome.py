#125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaner = ''.join([c for c in s.lower() if c.isalnum()])
        return cleaner == cleaner[::-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))