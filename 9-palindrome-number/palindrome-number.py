class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_number = x
        reverse_number = 0
        while x>0:
            digit = x % 10
            reverse_number = (reverse_number * 10) + digit
            x = x // 10

        if original_number == reverse_number:
            return True
        else:
            return False
    
