# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result=0
        self.dfs(root)
        if self.result>=2:
            return False
        else:
            return True
    
    def dfs(self,root):
        if not root:
            return 0

        left, right = self.dfs(root.left),self.dfs(root.right)

        if abs(left-right)>self.result:
            self.result = abs(left-right)

        return max(left,right)+1
