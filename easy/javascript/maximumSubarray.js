//https://leetcode.com/problems/maximum-subarray/

/**
 * @param {number[]} nums
 * @return {number}
 */
// var maxSubArray = function(nums) {
//     let sum = Math.max(...nums);
//     let maxSubarray = [nums.indexOf(sum)];

//     for(let subArrayStart = 0; subArrayStart < nums.length;subArrayStart++) {
//         let localSum = nums[subArrayStart];
//         let localSubArray = [nums[subArrayStart]]; 
//         for(let subArrayEnd = subArrayStart+1; subArrayEnd < nums.length;subArrayEnd++) {
//             localSum += nums[subArrayEnd];
//             localSubArray.push(nums[subArrayEnd]);
//             if (localSum > sum) {
//                 maxSubarray  = [...localSubArray];
//                 sum = localSum;
//             }
//         }
        

//     }
//     return sum
// };

var maxSubArray = function(nums) {
    let currentSum = 0;
    let maxSum = -Infinity;

    for(let i = 0; i < nums.length;i++) {
        if (currentSum > 0) {
            currentSum += nums[i];
        } else {
            currentSum = nums[i];
        }

        if ( currentSum > maxSum) {
            maxSum = currentSum
        }

    }
    return maxSum
};


array_1 = [-2,1,-3,4,-1,2,1,-5,4];

array_2 = [1];

array_3 = [5,4,-1,7,8];

console.log(maxSubArray(array_3));

