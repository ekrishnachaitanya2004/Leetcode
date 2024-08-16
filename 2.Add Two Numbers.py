
class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    a = ListNode(0)
    b = a
    c = 0

    while c or l1 or l2:
      if l1:
        c += l1.val
        l1 = l1.next
      if l2:
        c += l2.val
        l2 = l2.next
      b.next = ListNode(c % 10)
      c //= 10
      b = b.next

    return a.next