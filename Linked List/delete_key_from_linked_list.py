class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_key(head, key):
    dummy = ListNode(0)
    dummy.next = head
    current = head

    if dummy.next.val == key:
        return dummy.next.next
    while current.next:
        if current.next.val == key:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next
def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(22)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)

    result_ll = delete_key(ll, 1)
    print_linked_list(result_ll)