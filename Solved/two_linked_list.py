class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)

        # Move to the next nodes
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next

# Helper function to create a linked list from a list of numbers
def create_linked_list(numbers):
    dummy = ListNode()
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))

# Test case
l1 = create_linked_list([9, 9])
l2 = create_linked_list([5, 2])
result = add_two_numbers(l1, l2)
print_linked_list(result)  # Output: 4 -> 2 -> 1
