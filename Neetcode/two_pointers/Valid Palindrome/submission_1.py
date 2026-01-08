"""
Date: 01/07/2026 22:55
Memory: O(1)
Runtime: O(N)
"""

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # In: str s
        # Out: True/False --> Is s a palindrome?
        # Con:
        # - NOT case sensitive
        # - Ignores non-alphanumeric characters. --> char.isalnum()
        # Edge:
        # - empty string --> not possible
        # - string made up of all non-alphanumeric characters --> palindrome?

        left = 0
        right = len(s) - 1

        while left < right:
            print(left, right)
            # Move inward until both left and right are alphanumeric
            while not s[left].isalnum():
                left += 1
                if left >= right:
                    return True
            while not s[right].isalnum():
                right -= 1
                if left >= right:
                    return True
            # Compare
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True
"""

def isPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        print(left, right)
        # Move inward until both left and right are alphanumeric
        while not s[left].isalnum():
            left += 1
            if left >= right:
                return True
        while not s[right].isalnum():
            right -= 1
            if left >= right:
                return True
        # Compare
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True

# Test cases to be added
print(isPalindrome("Was it a car or a cat I saw?")) # True
print(isPalindrome("tab a cat")) # False