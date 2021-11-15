# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Solution 1 - Using Heap

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h = [(n.val,i,n) for i,n in enumerate(lists) if n]
        
        heapify(h)
        
        Head = ListNode()
        cur = Head
        
        while h!=[]:
            val, pos, Node = h[0]
            
            cur.next = Node
            cur = cur.next
            
            heappop(h)
            
            if Node.next:
                heappush(h, (Node.next.val, pos, Node.next))
                
            
        return Head.next   

# Solution 2 - Merge sorted lists

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0 : return None
        
        def mergeList(l1,l2):
            Node = ListNode()
            Head = Node
            while l1 and l2:
                if(l1.val < l2.val):
                    Node.next = l1
                    l1 = l1.next
                else:
                    Node.next = l2
                    l2 = l2.next
                Node = Node.next
            
            if l1:
                Node.next = l1
            if l2 :
                Node.next = l2
            return Head.next
        
        while(len(lists) > 1):
            mergedLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                mergedLists.append(mergeList(l1,l2))

            lists = mergedLists
        
        # print(lists)
        return lists[0]
        