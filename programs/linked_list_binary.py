class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def getDecimalValue(head: ListNode) -> int:
    num = 0
    while head is not None:
        num = num * 2 + head.val
        head = head.next
    return num
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example: binary number 101 represented in a linked list
values = [0, 0, 1,1,0,1,0]
linked_list_head = create_linked_list(values)

# Convert binary number in linked list to integer
result = getDecimalValue(linked_list_head)
print(result)  # Output: 5

########################################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def binary_to_integer(head):
    num = 0
    while head:
        num = num * 2 + head.val
        head = head.next
    return num

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

if __name__ == '__main__':
    values = [0, 0, 1, 1, 0, 1, 0]
    head = create_linked_list(values)
    result = binary_to_integer(head)
    print(result)  # Output: 26

