def findPeakElement(nums):
        n=len(nums)
       
        for i in range(n-1):
            
            if (nums[i]>nums[i+1] and nums[i]>nums[i-1]) or nums[0]>nums[1]:
                return i
            elif nums[n-1]>nums[n-2]:
                return i




#print(findPeakElement([1,2,3,1]))
#nums = [5,2,1,3,5,6,4]
#print(findPeakElement([1,2]))
#print()##
###ADDING TESTCASES
class TestPeakElement(unittest.TestCase):
    def test_list_one(self):
        actual=find_peak_element([1,2])
        expected=1
        self.assertEqual(actual,expected,"it should be 1")
    def test_list_two(self):
        actual=find_peak_element([1,2,3,4,1])
        expected=3
        self.assertEqual(actual,expected,"it should be 3")
        

if __name__ == "__main__":

    unittest.main()
