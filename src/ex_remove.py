#import numpy as np

#class Solution(object):
    #def productExceptSelf(self, nums):
    
        #n=len(nums)
        #result=[1]*n
        #result[0]=np.prod(nums[1:])
        #result[n-1]=np.prod(nums[:n-2])
        #for i in range(1,n-1,1):
            #inter=nums[:i-1]+nums[i+1:]
            #result[i]=np.prod(inter)

        #for i in range(n):
            #for j in range(n):
                #if j !=i:
                    #result[i]*=nums[j]
        #return result

#solution_instance = Solution()
nums = [1,2,3,4]
n=len(nums)
print(nums[:n-1])
#resultat = solution_instance.maxProfit(prices)
#print("Le profit max est:", resultat)