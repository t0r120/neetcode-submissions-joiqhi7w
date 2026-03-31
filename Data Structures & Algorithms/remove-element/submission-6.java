class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for(int index = 0; index < nums.length; index++){
            if (nums[index] != val){
                nums[k] = nums[index];
                k++;
            }
        }
        return k;


    }
}