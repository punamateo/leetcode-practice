/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let majorityMap = new Map();
    let majorityElem = nums[0];
    for (let i = 0; i < nums.length;i++) {
        if (majorityMap.has(nums[i])){
            let elemCount = majorityMap.get(nums[i]);
            majorityMap.set(nums[i], elemCount + 1);
        } else {
            majorityMap.set(nums[i], 1);
        }
        if (majorityMap.get(nums[i]) > majorityMap.get(majorityElem)) {
            majorityElem  =  nums[i];        
        }
    }

    return majorityElem
};

let arr = [2,2,1,1,1,2,2];

console.log(majorityElement(arr))

