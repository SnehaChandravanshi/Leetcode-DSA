class Solution:
    def findDuplicate(self, nums):
        
        slow = nums[0]
        fast = nums[0]

        # Step 1: Detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Step 2: Find entrance of cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow