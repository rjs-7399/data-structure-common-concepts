class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def insert_after_given_node(head, node_val):
    current = head
    while current:
        if current.val == node_val:
            new_node = ListNode(300)
            new_node.next = current.next
            current.next = new_node
            current = current.next
        else:
            current = current.next



if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)

    insert_after_given_node(ll, 1)
    print_linked_list(ll)