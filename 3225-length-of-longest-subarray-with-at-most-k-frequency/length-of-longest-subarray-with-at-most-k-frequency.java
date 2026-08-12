class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        int result = 0;
        int start = 0;
        Map<Integer, Integer> storage = new HashMap<>();
        for (int end = 0; end < nums.length; end++) {
            storage.put(nums[end], storage.getOrDefault(nums[end], 0) + 1);
            while (storage.get(nums[end]) > k) {
                storage.put(nums[start], storage.get(nums[start]) - 1);
                start++;
            }
            result = Math.max(result, end - start + 1);
        }
        return result;
    }
}