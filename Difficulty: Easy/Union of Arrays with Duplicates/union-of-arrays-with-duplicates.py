class Solution:
    def findUnion(self, a, b):
        # Use set to store unique elements
        union_set = set(a)
        
        # Add elements from second array
        for num in b:
            union_set.add(num)
        
        # Return sorted list
        return sorted(union_set)