/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        List<List<Integer>>  subList = new ArrayList<>();

         if (root != null){
            queue.add(root);
         }
        

         while(!queue.isEmpty()){

            List<Integer> level = new ArrayList<>();

            for(int i = queue.size(); i > 0; i--){
                
                TreeNode curr = queue.poll();

                if(curr != null){
                    level.add(curr.val);
                    queue.add(curr.left);
                    queue.add(curr.right);
                }
                
            }
            if (level.size() > 0){
                subList.add(level);

            }
            
        }return subList;
        
    }
}
