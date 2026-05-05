class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if flag==False:
            if (a>0 and b>0) or (a<0 and b<0):
                return False
            else: 
                return True
        elif flag==True:
            if a<0 and b<0:
                return True
            else:
                return False
        else: return False