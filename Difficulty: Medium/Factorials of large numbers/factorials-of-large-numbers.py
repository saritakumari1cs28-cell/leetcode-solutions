class Solution:
    def factorial(self, N):
        fact = 1
        
        # Calculate factorial
        for i in range(1, N + 1):
            fact *= i
        
        # Convert to list of digits
        result = []
        for digit in str(fact):
            result.append(int(digit))
        
        return result