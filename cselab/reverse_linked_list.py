"""Reverse a Linked List."""

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def from_list(values: list[int]) -> "ListNode | None":
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: "ListNode | None") -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def reverse_list(head: "ListNode | None") -> "ListNode | None":
    """Reverse the list in place and return the new head."""
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev
