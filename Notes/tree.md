### Tree Algorithms

#### Tree Traversal

##### In-order Traversal
In-order traversal produces sorted sequence for a BST. There are two implementations, namely  
*recursive algorithm* and *iterative algorithm*. 

> Recursive Algorithm

    inorder_recursive(root, values):
        if root is None:
            return 
        inorder_recursive(root.left, values)
        values.append(root.val)
        in_order.recursive(root.right, values)

> Iterative Algorithm

    inorder_iterative(root):
        values = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            
            elif stack:
                top = stack.pop()
                values.append(val)
                curr = top.right
        return values
                
   