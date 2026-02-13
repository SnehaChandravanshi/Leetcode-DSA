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
    int sum = 0;
    public int sumNumbers(TreeNode root) {
        int n = 0;
        sum(root,n);
        return sum;
    }
    public void sum(TreeNode root,int n){
        if(root==null) return ;
        n = n*10+root.val;
        if(root.left == null && root.right == null) {
            sum+= n;
            return ;
        }
        sum(root.left,n);
        sum(root.right,n);
    }
}