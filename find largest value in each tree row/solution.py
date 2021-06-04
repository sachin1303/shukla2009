# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = collections.deque()
        res = []
        queue.append(root)
        while queue:
            size = len(queue)
            max_level = float("-inf")
            for i in range(size):
                node = queue.popleft()
                if not node: continue
                max_level = max(max_level, node.val)
                queue.append(node.left)
                queue.append(node.right)
            if max_level != float("-inf"):
                res.append(max_level)
        return res

        