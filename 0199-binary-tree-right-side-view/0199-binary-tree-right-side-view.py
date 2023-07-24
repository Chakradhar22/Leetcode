# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = dict()
        self.func(root,d,0)
        return d.values()
    def func(self,root,d,level):
        if root is None:
            return
        if level not in d:
            d[level] = root.val
        self.func(root.right,d,level+1)
        self.func(root.left,d,level+1)