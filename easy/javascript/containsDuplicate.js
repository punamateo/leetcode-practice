//https://leetcode.com/problems/contains-duplicate/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const numsSet = new Set(nums);
    if (nums.length > numsSet.size) {
        return true
    }

    return false
};

[1,2,3,1]