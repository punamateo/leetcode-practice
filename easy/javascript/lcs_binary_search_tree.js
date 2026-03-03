// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


function TreeNode(val) {
      this.val = val;
      this.left = null;
      this.right = null;
  }

var binarySearchStack = function(root, node, stack) {
    if (root.val == node.val) {
        stack.push(node);
        return stack;
    } 

    stack.push(root)
    
    if (node.val > root.val) {
        return binarySearchStack(root.right, node, stack);
    } else if (node.val < root.val) {
        return binarySearchStack(root.left, node, stack);
    }
}

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    
    //binary search for each X
    //store nodes in stack X
    //after storing in both stacks, pop X
    var pStack = [];
    var qStack = [];

    pStack = binarySearchStack(root,p, pStack);
    qStack = binarySearchStack(root,q, qStack);

    var firstPop = null;
    var secondPop = null;

    if (pStack.length > qStack.length) {
        firstPop = pStack;
        secondPop = qStack;
    } else {
        firstPop = qStack;
        secondPop = pStack;
    }

    var lcs = null;
    var counter = 0;

    while (lcs == null) {
        var popped = null;
        var xLast = null;

        if (pStack.length > qStack.length) {
        firstPop = pStack;
        secondPop = qStack;
        } else {
            firstPop = qStack;
            secondPop = pStack;
        }

        var popped = firstPop.pop();
        xLast = secondPop[secondPop.length-1]

        if (popped == xLast){
            lcs = xLast;
        } 
        counter++;
    }
    return lcs;
}


// -----------------------Optimized solution---------------

const c1 = [6,2,8,0,4,7,9,null,null,3,2];

const tree = new TreeNode(6);
tree.left = new TreeNode(2);
tree.right = new TreeNode(8);
tree.left.left = new TreeNode(0);
tree.left.right = new TreeNode(4);
tree.right.left = new TreeNode(7);
tree.right.right = new TreeNode(9);
tree.left.right.left = new TreeNode(3);
tree.left.right.right = new TreeNode(5);


const lcs = lowestCommonAncestor(tree, new TreeNode(2), new TreeNode(8));
console.log(lcs)