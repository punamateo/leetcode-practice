// https://leetcode.com/problems/invert-binary-tree/

 function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

var invertTree = function(root) {
    if (root == null){
        console.log("")
        return null;
    }

    //node is a leaf.
    if (root.left == null && root.right == null) {
        return;
    }

    invertTree(root.left);
    invertTree(root.right);

    const oldLeft = root.left;
    root.left = root.right;
    root.right = oldLeft;  
}

const testCase1 = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7, new TreeNode(6), new TreeNode(9))); 
const testCase2 = [2,1,3]
const testCase3 = []

console.log(testCase1);
console.log("-------");
invertTree(testCase1)
console.log(testCase1)


//Tengo que realizar el analisis O(n) y el analisis amortizado
// 25 min vs 15 that it should take. Need to move faster!