class Solution:
    def findUnion(self, a, b):
        # Convert both arrays into a set to remove duplicates
        union_set = set(a) | set(b)
        
        # Return sorted list (as driver code expects sorted output)
        return sorted(union_set)