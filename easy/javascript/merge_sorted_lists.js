//https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode {
    constructor(val, next) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
 }

/**
* @param {ListNode} list1
* @param {ListNode} list2
* @return {ListNode}
*/
var mergeTwoLists = function(list1IterHead, list2IterHead) {

   let newHead =  new ListNode(0);

   let currentIterPointer = newHead;

   while (list1IterHead && list2IterHead) {

    if (list1IterHead.val <= list2IterHead.val) {
        currentIterPointer.next = new ListNode(list1IterHead.val);
        list1IterHead = list1IterHead.next;
        currentIterPointer = currentIterPointer.next;
    } else {
        currentIterPointer.next = new ListNode(list2IterHead.val)
        list2IterHead = list2IterHead.next;
        currentIterPointer = currentIterPointer.next;
    }    

   }

    currentIterPointer.next = list1IterHead || list2IterHead;
    return newHead.next;

}



function createLinkedList(array) {

    if (array.length == 0) {
        return null;
    }

    return new ListNode(array[0], createLinkedList(array.slice(1)));
}

function printLinkedList(listOfNodes) {

    let currentNode = listOfNodes;

    while (currentNode != null) {
        console.log(currentNode.val);
        currentNode = currentNode.next;
    }
}

let list1 = createLinkedList([1,2,4]);
let list2 = createLinkedList([1,3,4]);


const mergedLists = mergeTwoLists(list1, list2);

printLinkedList(mergedLists);
