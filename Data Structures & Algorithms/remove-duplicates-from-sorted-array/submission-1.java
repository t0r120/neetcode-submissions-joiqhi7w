class Solution {
    public int removeDuplicates(int[] nums) {

        int i = 1;
        int k = 0;

        for (int index = 0; index < nums.length; index++ ){
            if(nums[index] != nums[i - 1]){
                nums[i++] = nums[index];                 
            }
            k ++;
        }
        return i;


        
    }
}