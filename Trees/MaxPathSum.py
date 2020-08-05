class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxPathUtil(root):

    # if the root is null then we return 0
    if root is None:
        return 0


    # we get the max single path from the left subtree
    l = maxPathUtil(root.left)
    # and the right subtree
    r = maxPathUtil(root.right)

    # we include at most one child of the current root and
    # return the highest path sum
    max_single = max(max(l,r) + root.data, root.data)

    # we then find the max of the max path single and the sum of the path
    # without including the ancestors of the root
    max_top = max(max_single, l + r + root.data)

    # store the result in a static function
    maxPathUtil.res = max(maxPathUtil.res, max_top)
    # return the max_single to be used by the ancestor nodes
    return max_single
