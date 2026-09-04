# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()      # Create an "overarching" linkedlist, this will hold all the answer information as we traverse the other 2 lists 
        cur = dummy             # Create a pointer, this will always point to the end of the answer list "dummy", so we can append directly to the end!

        while list1 and list2:  
            if list1.val < list2.val:
                cur.next = list1     # Append the list which currently has the smaller value at the front to the current overarching list
                cur = list1          # move the pointer to the next value (the value of the newly appended list)
                list1 = list1.next   # move the list pointer to its next value (Or, for all intents and purposes, remove the appended value from the list) 
            
            # This is the exact same but for the other list
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        
        # The pointer is very good here, it is such that if there is anything left of the other 2 lists, just append it to the end
        cur.next = list1 if list1 else list2

        # What I'm wondering though, is that if these variables act more as pointers than storage devices, does the information of what is "no longer referenced" get removed from memory?
        # Say you have a list1 1-3-5-7 and another list2 2-4-6-8 and want to create a merged list 1-2-4-5-7-8 using the above method, would 3 and 6 be removed from memory as the listnode pointers move past them and no variables contain references to their memory?
        return dummy.next