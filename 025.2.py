def culc_num(node):
  left = culc_num(node.left) if node.left else 0
  right = culc_num(node.right) if node.right else 0
  node.val += right
  return(node.val+left)
