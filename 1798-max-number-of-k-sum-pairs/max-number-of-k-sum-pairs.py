class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #Try with hashmaps
        hashmap = {}
        counter = 0
        for num in nums:
            required = k - num
            if hashmap.get(required, 0) > 0:
                hashmap[required] -= 1
                counter += 1
            else:
                hashmap[num] = hashmap.get(num, 0) + 1
        return counter
            
        
        
            

    




        # Attempt 1 too slow
        # counter=0
        # leftpointer = 0
        # rightpointer = 1
        # required = 0
        # while True:
        #     required = k - nums[leftpointer]
        #     if required in nums[leftpointer+1:]:
        #         nums.pop(leftpointer)
        #         nums.remove(required)
        #         counter += 1
        #     else:
        #         leftpointer += 1
        #     if leftpointer >= len(nums):
        #         break
        # return counter

            

