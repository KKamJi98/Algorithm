# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check_balance(node):
            if not node:
                return 0

            left_height = check_balance(node.left)
            right_height = check_balance(node.right)

            if (
                left_height == -1
                or right_height == -1
                or abs(left_height - right_height) > 1
            ):
                return -1

            return max(left_height, right_height) + 1

        return check_balance(root) != -1
