def findPeakElement(nums):
        n=len(nums)
       
        for i in range(n-1):
            
            if (nums[i]>nums[i+1] and nums[i]>nums[i-1]) or nums[0]>nums[1]:
                return i
            elif nums[i]>nums[i-1]:
                return i




#print(findPeakElement([1,2,3,1]))
#nums = [5,2,1,3,5,6,4]
#print(findPeakElement([1,2]))
#print()
