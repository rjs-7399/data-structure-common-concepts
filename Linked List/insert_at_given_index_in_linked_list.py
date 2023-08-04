class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def insert_at_given_index(head, index, val):
    current = head
    ll_len = get_length(current)
    if index == 0:
        dummy = ListNode(val)
        dummy.next = current
        return dummy
    elif ll_len == index:
        dummy = ListNode(0)
        dummy.next = current
        while current.next:
            current = current.next
        current.next = ListNode(val)
        return dummy.next
    else:
        dummy = ListNode(0)
        dummy.next = current
        current_index = 0
        while current:
            current_index += 1
            if index == current_index:
                new_node = ListNode(val)
                new_node.next = current.next
                current.next = new_node
                #current = current.next
            else:
                current = current.next
        return dummy.next


if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    result_ll = insert_at_given_index(ll, 3, 300)
    print_linked_list(result_ll)