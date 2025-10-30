
// Intuition
// Describe your first thoughts on how to solve this problem.

// Approach
//  Describe your approach to solving the problem. 

// Complexity
//  - Time complexity:
// Add your time complexity here, e.g. $$O(n)$$

//  Space complexity:
// Add your space complexity here, e.g. $$O(n)$$ 

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */


var searchLogic = function(nums, target, indexArray) {
    half_index = Math.ceil(nums.length/2)

    // console.log(indexArray);

    if (nums.length == 1) {
        if (nums[0] == target) return nums
        if (nums[0] != target) return -1
    }

    if (target == nums[half_index]) {
        return indexArray[half_index]
    } else if (target < nums[half_index]) {
        return searchLogic(nums.slice(0,half_index),target, indexArray.slice(0,half_index));
    } else if (target > nums[half_index]) {
        return searchLogic(nums.slice(half_index, nums.length), target, indexArray.slice(half_index, indexArray.length));
    }


}
var search = function(nums, target) {
    lowest_num = nums[0];
    largest_num = nums[nums.length-1];

    if (target > largest_num) {
        return -1;
    }

    if (target < lowest_num) {
        return -1;
    }

    if (target == largest_num) {
        return nums.length-1;
    }

    if (target == lowest_num) {
        return 0;
    }
    var indexArray = [...Array(nums.length).keys()];
    index = searchLogic(nums, target, indexArray);
    return index
};

const target1 = 12;
const target2 = 15;
const testCase1 = [-1,0,3,5,9,12];



var index = search(testCase1, target2);
console.log(index)

// 28 min need to improve
// main errors syntax errors (very silly)
// I got confused running the wrong function
// I forgot to keep track of the index
// I got confused < with >