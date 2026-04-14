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
    public boolean isBalanced(TreeNode root) {

        return checkHeight(root) != -1;

    
    }

    private int checkHeight(TreeNode root){
        if (root == null) return 0;


        // Aim: To visit left SubTree
        int leftTree = checkHeight(root.left);
        if (leftTree == -1) return -1;


        // Aim: To visit right SubTree
        int rightTree =  checkHeight(root.right);
        if (rightTree == -1) return -1;


        //Calculates diference
        int balanced = Math.abs(leftTree - rightTree);
        
        if(balanced > 1) {
            return -1;
        }

        return Math.max(leftTree, rightTree) + 1;


    }
}
