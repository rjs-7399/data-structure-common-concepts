class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_length_of_linked_list(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)

    length = get_length_of_linked_list(ll)
    print(length)