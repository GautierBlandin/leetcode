from medium.add_two_numbers_linked_list.ListNode import ListNode


def add_two_numbers(l1: ListNode, l2: ListNode):
    unfinished_lists = [l1, l2]

    head = None
    prev = None

    carry = 0
    while unfinished_lists:
        total = sum((l.val for l in unfinished_lists)) + carry
        digit = total % 10
        carry = total // 10

        cur = ListNode(digit)

        if prev is not None:
            prev.next = cur
            prev = cur
        else:
            head = cur
            prev = cur

        unfinished_lists = [l.next for l in unfinished_lists if l.next is not None]

    if carry > 0:
        prev.next = ListNode(carry)

    return head
