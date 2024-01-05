class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        
        if string[0] == '-':
            return False
        
        for i in range(len(string) // 2):
            if string[i] != string[-(i+1)]:
                return False
        return True